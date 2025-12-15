# Connecting to Hugging Face Backend

This document explains how the frontend has been configured to connect to the Hugging Face deployed backend at `https://huzaifachhipa-rag-chatbot.hf.space`.

## Changes Made

### 1. Environment Configuration
- Updated `.env` file to set `REACT_APP_API_URL=https://huzaifachhipa-rag-chatbot.hf.space/api/v1/`
- This allows the frontend to connect to the Hugging Face backend instead of the local backend

### 2. Package Configuration
- Removed the `"proxy": "http://localhost:8000"` entry from `package.json`
- This allows the frontend to make requests to external domains instead of being limited to localhost

### 3. Frontend Logic
- Updated the Chatbot component (`src/components/Chatbot/index.tsx`) to ensure it uses the Hugging Face backend URL in production
- Modified the logic to default to the Hugging Face backend URL if the environment variable is not processed correctly during build

## How It Works

1. When the chatbot sends a message, it checks if running on localhost
2. If on localhost, it connects to `http://localhost:8000/api/v1/` for development
3. If in production (not localhost), it uses the `REACT_APP_API_URL` environment variable which is set to `https://huzaifachhipa-rag-chatbot.hf.space/api/v1/`
4. If for any reason the environment variable is not available, it defaults to the Hugging Face backend URL
5. The frontend makes POST requests to the Hugging Face backend
6. The backend processes the query and returns the response in the expected format
7. The frontend displays the response in the chat interface

## API Request Format
```json
{
  "query": "user input text"
}
```

## API Response Format
```json
{
  "answer": "response text",
  "evidence": [...],
  "confidence": "High|Medium|Low",
  "follow_up": {...}
}
```

## Testing
The connection was tested and confirmed working by making a direct API call to the Hugging Face backend and receiving a proper response.

## Common Issues & Troubleshooting

### Hugging Face Space Sleeping
- Hugging Face Spaces may go to sleep when not accessed for a while
- First request after sleep may timeout or fail
- **Solution**: Access your space directly at https://huzaifachhipa-rag-chatbot.hf.space/ to wake it up

### CORS (Cross-Origin Resource Sharing) Policy
- The backend is configured to allow requests from your domain: `https://robotics-book-kohl.vercel.app`
- When testing locally on `localhost`, browsers enforce CORS policies that prevent cross-origin requests
- **Solution**: The connection will work properly when the frontend is deployed to your Vercel domain

### Local Development vs Production
- **Local testing**: Frontend connects to `http://localhost:8000/api/v1/`
- **Production**: Frontend connects to `https://huzaifachhipa-rag-chatbot.hf.space/api/v1/`
- The chatbot is configured to handle both environments appropriately

### Improved Error Handling
- The chatbot now provides more specific error messages
- Distinguishes between network errors, CORS issues, and backend errors
- Debug logs help identify connection problems

## Deployment
When deploying the frontend, ensure that the `REACT_APP_API_URL` environment variable is set correctly in the deployment environment (e.g., Vercel).