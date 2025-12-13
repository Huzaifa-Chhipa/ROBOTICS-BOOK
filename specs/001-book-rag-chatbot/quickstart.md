# Quickstart: Book RAG Chatbot

## Overview
This guide provides a quick setup and usage guide for the Book RAG Chatbot system. The system allows users to ask questions about book content and receive answers based only on the ingested book material.

## Prerequisites
- Python 3.11+
- Qdrant vector database (can run locally or remotely)
- Google Gemini API key
- Cohere API key
- Book content available via sitemap.xml

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file with the following:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   COHERE_API_KEY=your_cohere_api_key_here
   QDRANT_URL=your_qdrant_instance_url
   QDRANT_API_KEY=your_qdrant_api_key
   QDRANT_COLLECTION_NAME=humanoid_ai_book
   COHERE_EMBED_MODEL=embed-english-v3.0
   GEMINI_MODEL=gemini-2.0-flash
   ```

## Setup and Configuration

1. **Initialize Qdrant collection**
   The system will automatically create the required collections in Qdrant on first run, but you can also set up manually:
   ```python
   from qdrant_client import QdrantClient

   client = QdrantClient(url="http://localhost:6333")
   # Collections will be created automatically by the ingestion service
   ```

2. **Ingest book content**
   ```bash
   python -m src.services.ingestion_service --sitemap-url https://book-website.com/sitemap.xml --book-title "Book Title"
   ```

## Running the Service

1. **Start the API server**
   ```bash
   uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Using Docker (recommended)**
   ```bash
   docker-compose up --build
   ```

3. **Or run with gunicorn for production**
   ```bash
   gunicorn src.api.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```

## Making Queries

### Using the API
```bash
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is the main concept discussed in the book?",
    "selected_chunks": []  // Optional: restrict to specific chunk IDs
  }'
```

### Expected Response Format
```json
{
  "answer": "The main concept discussed in the book is...",
  "evidence": [
    {
      "doc_id": "doc_123",
      "chunk_id": "chunk_456",
      "quote": "The main concept is..."
    }
  ],
  "confidence": "High",
  "follow_up": {
    "ask": true,
    "question": "Would you like to know more about this concept?"
  }
}
```

## Key Features

### Source-Based Answering
- Answers are generated only from ingested book content
- If no relevant passages are found, the system responds: "No supporting text found in the book."

### Selected Text Mode
- Restrict queries to specific content chunks by providing `selected_chunks` parameter
- If answer is not available in selected text, responds: "Answer not available in the selected text."

### Citations and Transparency
- All answers include evidence citations with document IDs and verbatim quotes
- Confidence levels (High/Medium/Low) indicate answer reliability
- Excerpts are limited to ≤200 characters as specified

## Troubleshooting

### Common Issues
1. **No results found**: Verify book content was properly ingested and embeddings were created
2. **API errors**: Check that Gemini API key, Cohere API key, and Qdrant connection are properly configured
3. **Slow responses**: Check Qdrant performance and consider optimizing embedding search parameters
4. **Validation errors**: Ensure selected chunk IDs exist in the database when using selected text mode

### Environment Setup
- Ensure Qdrant is running and accessible
- Verify Gemini API key has appropriate permissions
- Verify Cohere API key has appropriate permissions
- Check that the sitemap.xml is accessible and properly formatted

## Next Steps
- Explore the API documentation at `/docs` when the server is running
- Review the contract definitions in the `contracts/` directory
- Check out the comprehensive test suite in the `tests/` directory
- Run tests with: `pytest tests/`