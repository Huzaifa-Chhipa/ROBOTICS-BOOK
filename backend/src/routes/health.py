"""
Health check API routes for the Book RAG Chatbot.
"""
from fastapi import APIRouter
from pydantic import BaseModel
from ..services.qdrant_service import check_connection as check_qdrant
from ..services.openai_service import check_connection as check_gemini
from ..services.cohere_service import check_connection as check_cohere
import datetime

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    dependencies: dict

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify service status.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "dependencies": {
            "qdrant": await check_qdrant(),
            "cohere": await check_cohere(),
            "gemini": await check_gemini()
        }
    }
