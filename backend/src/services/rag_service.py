"""
RAG service for the Book RAG Chatbot.
Implements query interpretation and retrieval strategy.
"""
from typing import List, Dict, Any, Optional
import asyncio
# Import compatibility patch before importing agents
from ..tf_compat_patch import *

# Try to import function_tool from agents, with fallback if not available
try:
    from agents import function_tool
except ImportError:
    # If function_tool is not available from agents, create a mock decorator
    def function_tool(func):
        """Mock function_tool decorator for compatibility."""
        return func
from ..models.query import UserQuery
from ..models.retrieved_passages import RetrievedPassages, RetrievedPassage
from ..models.response import Response, Evidence
from .qdrant_service import query_points
from ..utils.validation_utils import (
    validate_response_based_on_retrieved_content,
    validate_chunk_ids_exist
)
from ..agents.chatbot_agent import process_with_agent
import uuid
import datetime

def retrieve(query: str, selected_chunks: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Retrieve function with Qdrant vector database search.

    Args:
        query: The user's query to search for relevant content
        selected_chunks: Optional list of specific chunk IDs to restrict search to

    Returns:
        Dictionary containing retrieved passages and metadata
    """
    try:
        # Call the Qdrant service to retrieve relevant passages
        result = query_points(
            query=query,
            limit=5,
            selected_chunks=selected_chunks
        )

        return {
            "passages": result["passages"],
            "found_content": result["found_content"],
            "raw_points": result["points"]  # Include raw points if needed for more detailed processing
        }
    except Exception as e:
        print(f"Error during retrieval: {e}")
        return {
            "passages": [],
            "found_content": False,
            "error": str(e)
        }

async def process_query(
    user_input: str,
    selected_chunks: Optional[List[str]] = None
) -> Response:
    """
    Process a user query through the RAG system

    Args:
        user_input: The user's question
        selected_chunks: Optional list of specific chunk IDs to restrict search to

    Returns:
        Response with answer, evidence, confidence, and follow-up
    """
    # Generate IDs
    query_id = str(uuid.uuid4())
    response_id = str(uuid.uuid4())

    # Create user query object
    user_query = UserQuery(
        id=query_id,
        text=user_input,
        selected_chunks=selected_chunks or []
    )

    # Validate selected chunks if provided
    if selected_chunks:
        # In a real implementation, we would validate against actual available chunk IDs in Qdrant
        # For now, we'll implement basic validation
        from ..utils.validation_utils import validate_chunk_ids_exist

        # This is a simplified validation - in a real system you'd check against the actual database
        # For now, we'll just validate the format
        for chunk_id in selected_chunks:
            if not isinstance(chunk_id, str) or not chunk_id.strip():
                raise ValueError(f"Invalid chunk ID format: {chunk_id}")

    # Retrieve relevant passages from vector database using the tool function
    retrieval_result = retrieve(
        query=user_input,
        selected_chunks=selected_chunks
    )

    # Check if there was an error during retrieval
    if "error" in retrieval_result and retrieval_result["error"]:
        # Return an appropriate error response
        return Response(
            id=response_id,
            query_id=query_id,
            answer="Error retrieving information from the knowledge base. Please try again later.",
            evidence=[],
            confidence="Low",
            follow_up={"ask": False, "question": ""},
            timestamp=datetime.datetime.now(),
            json_schema={}
        )

    # Check if we found relevant content
    if not retrieval_result["found_content"]:
        # Check if specific chunks were requested (selected text mode)
        if selected_chunks and len(selected_chunks) > 0:
            # Return the specified response when selected text doesn't contain answer
            return Response(
                id=response_id,
                query_id=query_id,
                answer="Answer not available in the selected text.",
                evidence=[],
                confidence="Low",
                follow_up={"ask": False, "question": ""},
                timestamp=datetime.datetime.now(),
                json_schema={}
            )
        else:
            # Return the specified response when no content is found in general search
            return Response(
                id=response_id,
                query_id=query_id,
                answer="No supporting text found in the book.",
                evidence=[],
                confidence="Low",
                follow_up={"ask": False, "question": ""},
                timestamp=datetime.datetime.now(),
                json_schema={}
            )

    # Process with the agent using the retrieved passages
    agent_response = await process_with_agent(
        user_input=user_input,
        retrieved_passages=retrieval_result["passages"]
    )

    # Calculate confidence based on similarity scores
    similarity_scores = retrieval_result.get("similarity_scores", [])
    confidence = calculate_confidence(similarity_scores)

    # Create evidence objects from the retrieved passages with proper metadata
    evidence_list = []
    for i, passage in enumerate(retrieval_result["passages"][:3]):  # Limit to first 3 passages
        # Extract document and chunk IDs from the raw points if available
        doc_id = "unknown"
        chunk_id = f"chunk_{i}"

        # Try to extract more meaningful IDs from the raw points
        if "raw_points" in retrieval_result and i < len(retrieval_result["raw_points"]):
            point = retrieval_result["raw_points"][i]
            if hasattr(point, 'payload') and point.payload:
                doc_id = point.payload.get("doc_id", f"doc_{i}")
                chunk_id = point.payload.get("chunk_id", f"chunk_{i}")

        evidence = Evidence(
            doc_id=doc_id,
            chunk_id=chunk_id,
            quote=passage  # Full passage without truncation
        )
        evidence_list.append(evidence)

    # Create and return the response
    response = Response(
        id=response_id,
        query_id=query_id,
        answer=agent_response,
        evidence=evidence_list,
        confidence=confidence,
        follow_up={"ask": True, "question": "Do you have any follow-up questions?"},
        timestamp=datetime.datetime.now(),
        json_schema={
            "answer": agent_response,
            "evidence": [e.dict() for e in evidence_list],
            "confidence": confidence,
            "follow_up": {"ask": True, "question": "Do you have any follow-up questions?"}
        }
    )

    # Validate the response to ensure it's based only on retrieved passages
    is_valid = validate_response_based_on_retrieved_content(
        response.answer,
        retrieval_result["passages"]
    )

    if not is_valid and "No supporting text found in the book." not in response.answer:
        # If validation fails, return a safe response
        return Response(
            id=response_id,
            query_id=query_id,
            answer="No supporting text found in the book.",
            evidence=[],
            confidence="Low",
            follow_up={"ask": False, "question": ""},
            timestamp=datetime.datetime.now(),
            json_schema={}
        )

    return response


def calculate_confidence(similarity_scores: List[float]) -> str:
    """
    Calculate confidence level based on similarity scores

    Args:
        similarity_scores: List of similarity scores from vector search

    Returns:
        Confidence level as "High", "Medium", or "Low"
    """
    if not similarity_scores:
        return "Low"

    avg_score = sum(similarity_scores) / len(similarity_scores)

    if avg_score >= 0.7:
        return "High"
    elif avg_score >= 0.4:
        return "Medium"
    else:
        return "Low"