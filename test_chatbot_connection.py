# Test script to verify the chatbot connection
import requests
import json

def test_chatbot_connection():
    """
    Test script to verify that the chatbot API endpoint is working correctly.
    This simulates what the frontend would do when sending a message.
    """
    # The API endpoint - this should match what the frontend uses
    api_url = "http://localhost:8000/api/v1/"

    # Test query
    test_data = {
        "query": "What is physical AI?",
        "selected_chunks": None
    }

    print("Testing chatbot API connection...")
    print(f"Sending request to: {api_url}")
    print(f"Query: {test_data['query']}")

    try:
        # Make the API call
        response = requests.post(
            api_url,
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            result = response.json()
            print("\n✅ Connection successful!")
            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(result, indent=2)}")
        else:
            print(f"\n❌ API returned error: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.ConnectionError:
        print("\n❌ Connection failed. Is the backend server running on http://localhost:8000?")
        print("To start the backend, run: python -m backend.src.main")
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")

if __name__ == "__main__":
    test_chatbot_connection()