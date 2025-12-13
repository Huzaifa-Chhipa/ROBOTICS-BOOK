"""
Health check API routes for the Book RAG Chatbot.
"""
from fastapi import APIRouter
from pydantic import BaseModel

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
    import datetime
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "dependencies": {
            "qdrant": "checking...",
            "cohere": "checking...",
            "gemini": "checking..."
        }
    }