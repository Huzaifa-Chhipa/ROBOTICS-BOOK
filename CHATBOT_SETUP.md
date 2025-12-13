# Chatbot Setup Guide

This guide explains how to set up and run the AI chatbot for the Physical AI & Humanoid Robotics textbook.

## Overview

The chatbot is a Retrieval-Augmented Generation (RAG) system that allows users to ask questions about the robotics textbook content. It consists of:

- **Backend**: FastAPI server with AI processing and Qdrant vector database
- **Frontend**: Docusaurus-based documentation site with embedded chatbot widget
- **Connection**: REST API communication between frontend and backend

## Prerequisites

- Python 3.9+
- Node.js 18+
- Access to API keys (Gemini, Cohere, Qdrant)

## Setup Instructions

### 1. Environment Configuration

Copy the environment variables to your `.env` file:

```bash
# Gemini API configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Cohere API configuration
COHERE_API_KEY=your_cohere_api_key_here

# Qdrant vector database configuration
QDRANT_URL=your_qdrant_url_here
QDRANT_API_KEY=your_qdrant_api_key_here

# Optional: Additional configuration
QDRANT_COLLECTION_NAME=humanoid_ai_book
COHERE_EMBED_MODEL=embed-english-v3.0
GEMINI_MODEL=gemini-2.0-flash

# Frontend API configuration (for Docusaurus build)
REACT_APP_API_URL=/api/v1/
```

### 2. Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the backend server:
```bash
python -m src.main
```

The backend will start on `http://localhost:8000`.

### 3. Frontend Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Build the Docusaurus site:
```bash
npm run build
```

3. Start the development server:
```bash
npm start
```

The frontend will start on `http://localhost:3000`.

## API Connection Details

The frontend chatbot connects to the backend via the following endpoints:

- **Chat endpoint**: `POST /api/v1/` - Processes user queries
- **Health check**: `GET /api/v1/health` - Checks service status

The connection is configured to work in multiple environments:

- **Development**: Automatically detects localhost and connects to backend at `http://localhost:8000/api/v1/`
- **Production**: Uses relative path `/api/v1/` when served from the same domain as backend

## How the Chatbot Works

1. User types a question in the floating chatbot widget
2. Frontend sends the query to the backend API at `/api/v1/`
3. Backend retrieves relevant passages from Qdrant vector database
4. Backend processes the query with AI agent using retrieved context
5. Backend returns structured response with answer and evidence
6. Frontend displays the response in the chat interface

## Troubleshooting

### Common Issues

1. **CORS errors**: Make sure the backend allows requests from the frontend origin
2. **API key errors**: Verify all API keys are valid and properly configured
3. **Connection errors**: Check that backend is running and accessible

### Testing the Connection

To test if the backend API is working:

```bash
curl -X POST http://localhost:8000/api/v1/ \
  -H "Content-Type: application/json" \
  -d '{"query": "What is physical AI?"}'
```

## Deployment

For production deployment:

1. Build the Docusaurus frontend with `npm run build`
2. The backend serves the static files from the `build` directory
3. Set appropriate environment variables for your deployment environment
4. The chatbot will connect to the backend API automatically

The system is designed to work as a unified application where both frontend and backend run on the same domain, avoiding CORS issues.