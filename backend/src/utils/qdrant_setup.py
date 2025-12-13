"""
Qdrant collection setup utility for the Book RAG Chatbot.
"""
from qdrant_client import QdrantClient, models
from src.config import QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION_NAME

def create_collection():
    """
    Create the Qdrant collection for storing book content embeddings.
    """
    # Connect to Qdrant
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY
    )

    # Define the collection configuration
    # We'll assume Cohere's embedding dimension (typically 1024 for embed-english-v3.0)
    vector_size = 1024  # Adjust based on your Cohere model's embedding size

    # Check if collection already exists
    try:
        client.get_collection(QDRANT_COLLECTION_NAME)
        print(f"Collection '{QDRANT_COLLECTION_NAME}' already exists.")
        return
    except:
        print(f"Collection '{QDRANT_COLLECTION_NAME}' does not exist. Creating it...")

    # Create the collection
    client.create_collection(
        collection_name=QDRANT_COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE  # Cosine distance is common for embeddings
        )
    )

    print(f"Collection '{QDRANT_COLLECTION_NAME}' created successfully!")
    print(f"Collection will store robotics book content with embeddings of size {vector_size}")

if __name__ == "__main__":
    create_collection()