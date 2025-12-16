"""
Qdrant service for the Book RAG Chatbot.
"""
from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Dict, Any, Optional
from ..config import QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION_NAME
from ..utils.embedding_utils import get_embeddings_batch

# Connect to Qdrant
qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)


async def check_connection():
    """
    Check if Qdrant connection is available.

    Returns:
        str: "healthy" if connection is successful, "unhealthy" otherwise
    """
    try:
        # Try to list collections to verify connection
        qdrant.get_collection(QDRANT_COLLECTION_NAME)
        return "healthy"
    except Exception as e:
        print(f"Qdrant connection check failed: {e}")
        return "unhealthy"

def query_points(
    query: str,
    limit: int = 10,
    selected_chunks: Optional[List[str]] = None
) -> Dict[str, Any]:
    try:
        # Get embedding for the query (batch API)
        query_embedding = get_embeddings_batch([query])[0]

        # Prepare filter if specific chunks are selected
        query_filter = None
        if selected_chunks and len(selected_chunks) > 0:
            query_filter = models.Filter(
                must=[
                    models.FieldCondition(
                        key="chunk_id",
                        match=models.MatchAny(any=selected_chunks)
                    )
                ]
            )

        # Use query_points with correct parameters
        result = qdrant.query_points(
            collection_name=QDRANT_COLLECTION_NAME,
            query=query_embedding,
            limit=limit,
            query_filter=query_filter
        )

        passages = []
        for point in result.points:  # Access the points attribute of QueryResponse
            if "text" in point.payload:
                passages.append(point.payload["text"])

        similarity_scores = [point.score for point in result.points if hasattr(point, 'score')]

        return {
            "passages": passages,
            "points": result.points,  # Return the list of points, not the full response
            "similarity_scores": similarity_scores,
            "found_content": len(passages) > 0
        }

    except Exception as e:
        print(f"Error during Qdrant query: {e}")
        return {
            "passages": [],
            "points": [],
            "similarity_scores": [],
            "found_content": False,
            "error": str(e)
        }
