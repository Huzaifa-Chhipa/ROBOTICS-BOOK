"""
Main FastAPI application entry point for the Book RAG Chatbot.
"""
# Import TensorFlow compatibility patch first to handle deprecated tf.contrib.distributions
from .tf_compat_patch import *

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import os

from .routes import chat, health

app = FastAPI(
    title="Book RAG Chatbot API",
    description="A Retrieval-Augmented Generation chatbot for book content using OpenAI Agent SDK and Qdrant",
    version="1.0.0"
)

# Add CORS middleware to allow requests from the Docusaurus frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",  # Allow all for development
        "https://robotics-book-gamma.vercel.app",  # Your production domain
        "https://robotics-book-gamma-git-main-huzaifachhipas-projects.vercel.app",  # Vercel preview deployments
        "http://localhost:3000",  # Local Docusaurus development
        "http://localhost:8000",  # Local backend development
        "http://localhost:7860",  # Local backend development (FastAPI default)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the absolute path for static files (relative to project root)
current_file_path = Path(__file__).resolve()
static_dir = current_file_path.parent.parent.parent / "build"

# Serve static files only if the directory exists
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
else:
    print(f"Warning: Static files directory '{static_dir}' does not exist. Skipping static file serving.")

# Include API routes
app.include_router(chat.router, prefix="/api/v1", tags=["chat"])
app.include_router(health.router, prefix="/api/v1", tags=["health"])

# Serve the main UI page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Get the absolute path for the index.html file
    current_file_path = Path(__file__).resolve()
    build_dir = current_file_path.parent.parent.parent / "build"
    index_file_path = build_dir / "index.html"

    # Check if file exists first
    if not index_file_path.exists():
        # Return a simple informational page instead of an error
        return HTMLResponse(content="""
        <html>
            <head><title>Book RAG Chatbot API</title></head>
            <body>
                <h1>Book RAG Chatbot API</h1>
                <p>API is running successfully!</p>
                <p>Available endpoints:</p>
                <ul>
                    <li><a href="/docs">API Documentation</a></li>
                    <li><a href="/api/v1/health">Health Check</a></li>
                </ul>
                <p>To use the API, make POST requests to <code>/api/v1/</code> with JSON data.</p>
            </body>
        </html>
        """)

    with open(index_file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return HTMLResponse(content=content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)