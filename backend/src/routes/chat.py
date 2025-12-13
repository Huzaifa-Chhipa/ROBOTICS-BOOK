"""
Chat API routes for the Book RAG Chatbot.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ..services.rag_service import process_query

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    selected_chunks: Optional[List[str]] = None

class Evidence(BaseModel):
    doc_id: str
    chunk_id: str
    quote: str

class QueryResponse(BaseModel):
    answer: str
    evidence: List[Evidence]
    confidence: str
    follow_up: dict

@router.post("/", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    """
    Process a user query and return a response based on book content.
    """
    try:
        # Process the query through the RAG service
        result = await process_query(
            user_input=request.query,
            selected_chunks=request.selected_chunks
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))