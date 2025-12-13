"""
OpenAI service for the Book RAG Chatbot using Gemini API.
"""
# Import compatibility patch before importing agents
from ..tf_compat_patch import *
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents import set_tracing_disabled
import os
from src.config import GEMINI_API_KEY

# Configure Gemini API provider using OpenAI-compatible endpoint
provider = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Configure the model to use Gemini
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

def get_gemini_model():
    """
    Get the configured Gemini model for use in agents.

    Returns:
        OpenAIChatCompletionsModel configured for Gemini API
    """
    return model

def get_gemini_provider():
    """
    Get the configured Gemini API provider.

    Returns:
        AsyncOpenAI provider configured for Gemini API
    """
    return provider