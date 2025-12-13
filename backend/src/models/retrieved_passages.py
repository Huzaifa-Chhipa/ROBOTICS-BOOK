"""
Retrieved Passages model for the Book RAG Chatbot.
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import datetime

class RetrievedPassage(BaseModel):
    """Model representing a retrieved text segment from the vector database based on semantic similarity"""
    chunk_id: str = Field(..., description="Identifier of the retrieved content chunk")
    document_id: str = Field(..., description="Identifier of the source document")
    content: str = Field(..., description="The actual text content of the retrieved passage")
    similarity_score: float = Field(..., ge=0.0, le=1.0, description="Similarity score from vector search (0.0-1.0)")
    source_url: Optional[str] = Field(None, description="URL where the content originated")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata about the source")

class RetrievedPassages(BaseModel):
    """Collection of retrieved passages"""
    passages: List[RetrievedPassage] = Field(default_factory=list, description="List of retrieved passages")
    query_embedding: List[float] = Field(..., description="The embedding used for the query")
    search_limit: int = Field(default=5, description="The limit used for the search")
    found_content: bool = Field(default=False, description="Whether any content was found")
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now, description="When the retrieval was performed")