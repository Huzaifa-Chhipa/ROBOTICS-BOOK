"""
Cohere service for the Book RAG Chatbot.
"""
import os
from ..config import COHERE_API_KEY


async def check_connection():
    """
    Check if Cohere API connection is available.

    Returns:
        str: "healthy" if connection is successful, "unhealthy" otherwise
    """
    try:
        import cohere
        # Try to initialize the Cohere client and make a simple call
        co = cohere.AsyncClient(api_key=COHERE_API_KEY)
        # Make a simple test call using the generate method (more reliable for health check)
        response = await co.generate(
            model='command-r',
            prompt="test",
            max_tokens=1
        )
        return "healthy"
    except Exception as e:
        print(f"Cohere API connection check failed: {e}")
        return "unhealthy"