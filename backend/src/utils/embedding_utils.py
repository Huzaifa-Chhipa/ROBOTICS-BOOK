"""
Embedding utilities for the Book RAG Chatbot using Cohere.
Optimized for free-tier usage by batching requests.
"""

import cohere
from typing import List
from src.config import COHERE_API_KEY, COHERE_EMBED_MODEL

# Initialize Cohere client
cohere_client = cohere.Client(COHERE_API_KEY)


def get_embeddings_batch(texts: List[str], batch_size: int = 50) -> List[List[float]]:
    """
    Get embeddings in safe batches to avoid Cohere 429 rate limits.

    Args:
        texts: List of text chunks
        batch_size: Number of texts per API call

    Returns:
        List of embeddings
    """
    all_embeddings = []

    for start in range(0, len(texts), batch_size):
        batch = texts[start:start + batch_size]

        try:
            response = cohere_client.embed(
                model=COHERE_EMBED_MODEL,
                input_type="search_document",
                texts=batch
            )
            all_embeddings.extend(response.embeddings)

        except Exception as e:
            print(f"[EMBED ERROR] batch starting at index {start}: {e}")
            raise

    return all_embeddings


def get_query_embedding(query: str) -> List[float]:
    """
    ONLY for search queries at retrieval time, not ingestion.
    """
    try:
        response = cohere_client.embed(
            model=COHERE_EMBED_MODEL,
            input_type="search_query",
            texts=[query],
        )
        return response.embeddings[0]
    except Exception as e:
        print(f"[QUERY EMBED ERROR] {e}")
        raise
