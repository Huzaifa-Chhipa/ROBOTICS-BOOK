"""
Chatbot agent for the Book RAG Chatbot using OpenAI Agent SDK with Gemini API.
"""
import asyncio
from typing import List

# Try to import from agents with fallbacks for missing functions
try:
    from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI
    import agents
    from agents import set_tracing_disabled, function_tool
    from agents import enable_verbose_stdout_logging
except ImportError as e:
    # Handle missing functions with mocks
    print(f"Warning: agents package import issue: {e}")

    # Define placeholder classes that will raise errors only when instantiated/called
    class Agent:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("Agent not available - need to install correct agents package")

    class OpenAIChatCompletionsModel:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("OpenAIChatCompletionsModel not available")

    class AsyncOpenAI:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("AsyncOpenAI not available")

    def set_tracing_disabled(**kwargs):
        pass

    def function_tool(func):
        return func

    def enable_verbose_stdout_logging():
        pass

    import agents

import os
from dotenv import load_dotenv
from ..config import GEMINI_API_KEY

# Enable logging and setup
enable_verbose_stdout_logging()
load_dotenv()
set_tracing_disabled(disabled=True)

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

    AGENT_AVAILABLE = True
except (NotImplementedError, NameError):
    # Agents not available, set a flag
    AGENT_AVAILABLE = False
    provider = None
    model = None

def create_retrieve_tool(retrieved_passages: List[str]):
    """
    Create a retrieve tool that returns the pre-retrieved passages.
    This allows the agent to work with the passages already retrieved by the RAG service.
    """
    @function_tool
    def retrieve_tool(query: str) -> List[str]:
        """
        Tool for the agent to retrieve relevant passages from the vector database.
        """
        # Return the pre-retrieved passages that were passed to the agent
        return retrieved_passages

    return retrieve_tool

def create_agent_with_passages(retrieved_passages: List[str]):
    """
    Create an agent with the specific retrieved passages available via the retrieve_tool.
    """
    if not AGENT_AVAILABLE:
        raise NotImplementedError("Agents not available - cannot create agent")

    # Create the retrieve tool with the specific passages
    retrieve_tool = create_retrieve_tool(retrieved_passages)

    # Create the agent with specific instructions that follow constitutional principles
    agent = Agent(
        name="Humanoid Robotics AI Tutor",
        instructions="""
You are an AI tutor for the Physical AI & Humanoid Robotics textbook.
To answer the user question, first call the tool `retrieve_tool` with the user query.
Use ONLY the returned content from `retrieve_tool` to answer.
If the answer is not in the retrieved content, respond with exactly: "No supporting text found in the book."
If the user provided specific selected text and the answer is not in that selected text, respond with exactly: "Answer not available in the selected text."
Never invent facts or use external knowledge.
Always cite the source of your information when possible.
Keep answers concise, factual, and directly tied to retrieved passages.
When quoting, keep quotes short and exact (≤200 characters).
""",
        model=model,
        tools=[retrieve_tool]
    )

    return agent

async def process_with_agent(user_input: str, retrieved_passages: List[str]) -> str:
    """
    Process user input with the agent using retrieved passages.

    Args:
        user_input: The user's question
        retrieved_passages: List of passages retrieved from the vector database

    Returns:
        The agent's response to the user's question
    """
    if not AGENT_AVAILABLE:
        # If agents are not available, try to create a synthesized response based on the retrieved passages
        if retrieved_passages:
            # Try to find relevant content in the passages that answers the user's question
            user_question_lower = user_input.lower()
            relevant_content = []

            # Look for passages that might contain relevant information to the question
            for passage in retrieved_passages:
                passage_lower = passage.lower()
                # Simple keyword matching to find most relevant passages
                if any(keyword in passage_lower for keyword in user_question_lower.split()[:5]):  # Check first 5 words of question
                    relevant_content.append(passage)

            # If we found relevant content, create a response based on it
            if relevant_content:
                response = f"Regarding your question about '{user_input}', here's what the book says:\n\n"
                response += "\n\n".join(relevant_content[:2])  # Limit to 2 most relevant passages
            else:
                # If no specific relevance found, return the first few passages
                response = f"Here's information from the book related to your query:\n\n"
                response += "\n\n".join(retrieved_passages[:2])

            return response
        else:
            return "No supporting text found in the book."

    try:
        # Create an agent with the specific retrieved passages
        agent = create_agent_with_passages(retrieved_passages)

        # If no passages were retrieved, return the appropriate response
        if not retrieved_passages:
            return "No supporting text found in the book."

        # Create AgentRunner and run the agent with the user's question
        # The agent will call the retrieve_tool internally to get the passages
        agent_runner = agents.run.AgentRunner()
        result = await agent_runner.run(
            starting_agent=agent,
            input=user_input
        )

        # Extract the response content
        if result and hasattr(result, 'messages') and result.messages:
            response_content = result.messages[-1].content
            return response_content
        else:
            # Fallback if the agent didn't produce a proper response
            response_text = f"Based on the retrieved information: {' '.join(retrieved_passages)}"
            return response_text

    except Exception as e:
        print(f"Error processing with agent: {e}")
        # Fallback: return the retrieved passages directly when agent fails
        if retrieved_passages:
            fallback_response = "Based on the book content:\n\n" + "\n\n".join(retrieved_passages)
            return fallback_response
        else:
            return "No supporting text found in the book."