"""
Test script for RAG Chatbot query functionality
"""
import requests
import json

BASE_URL = "http://localhost:7860/api/v1"

def test_query(query_text):
    """Test a single query against the RAG chatbot"""
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "query": query_text,
        "selected_chunks": None
    }

    try:
        response = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()
        print(f"Query: {query_text}")
        print(f"Answer: {result.get('answer', 'No answer')}")
        print(f"Confidence: {result.get('confidence', 'N/A')}")
        print(f"Number of evidence sources: {len(result.get('evidence', []))}")
        print("-" * 80)
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

def main():
    """Run multiple test queries"""
    print("Testing RAG Chatbot Query Functionality")
    print("=" * 80)

    # Test queries related to the textbook content
    test_queries = [
        "What is humanoid robotics?",
        "Explain bipedal locomotion in humanoid robots",
        "What are the core capabilities of humanoid robots?",
        "How do humanoid robots achieve balance?",
        "What are the challenges in humanoid robotics?"
    ]

    for query in test_queries:
        test_query(query)

    # Test a query not related to the textbook
    print("Testing with a query not in the textbook:")
    test_query("What is the capital of France?")

if __name__ == "__main__":
    main()