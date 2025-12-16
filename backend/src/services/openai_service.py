"""
OpenAI service for the Book RAG Chatbot using Gemini API.
"""
# Import compatibility patch before importing agents
from ..tf_compat_patch import *

# Try to import from agents with fallbacks for missing functions
try:
    from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
    from agents import set_tracing_disabled

except ImportError as e:
    # Handle missing functions with mocks
    print(f"Warning: agents package import issue in openai_service: {e}")

    def Agent(*args, **kwargs):
        raise NotImplementedError("Agent not available")

    def Runner(*args, **kwargs):
        raise NotImplementedError("Runner not available")

    def OpenAIChatCompletionsModel(*args, **kwargs):
        raise NotImplementedError("OpenAIChatCompletionsModel not available")

    def AsyncOpenAI(*args, **kwargs):
        raise NotImplementedError("AsyncOpenAI not available")

    def set_tracing_disabled(**kwargs):
        pass

import os
from ..config import GEMINI_API_KEY

# Configure Gemini API provider using OpenAI-compatible endpoint
try:
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
except NotImplementedError:
    # Fallback functions when agents are not available
    def get_gemini_model():
        raise NotImplementedError("Agents not available - cannot get Gemini model")

    def get_gemini_provider():
        raise NotImplementedError("Agents not available - cannot get Gemini provider")


async def check_connection():
    """
    Check if Gemini API connection is available.

    Returns:
        str: "healthy" if connection is successful, "unhealthy" otherwise
    """
    try:
        # Try to make a simple API call to check connection
        from openai import AsyncOpenAI
        client = AsyncOpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        # Make a simple test call
        chat_completion = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[
                {"role": "user", "content": "test"}
            ],
            max_tokens=1
        )
        return "healthy"
    except Exception as e:
        print(f"Gemini API connection check failed: {e}")
        return "unhealthy"