"""
User Query model for the Book RAG Chatbot.
"""
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
import datetime

class UserQuery(BaseModel):
    """Model representing a user's question or request to the system"""
    id: str
    text: str = Field(..., min_length=1, max_length=1000, description="The natural language question from the user")
    selected_chunks: Optional[List[str]] = Field(
        default_factory=list,
        description="Optional list of specific chunk IDs to restrict search to"
    )
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now, description="When the query was submitted")
    session_id: Optional[str] = Field(None, description="Optional session identifier for conversation context")

    class Config:
        # Allow extra fields for flexibility
        extra = "allow"

    @field_validator('selected_chunks')
    @classmethod
    def validate_selected_chunks(cls, v):
        """Validate that selected chunks are properly formatted"""
        if v is None:
            return v

        # Ensure all chunk IDs are non-empty strings
        for chunk_id in v:
            if not isinstance(chunk_id, str) or not chunk_id.strip():
                raise ValueError(f"Invalid chunk ID: {chunk_id}")

        return v