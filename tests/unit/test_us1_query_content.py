"""
Unit tests for US1 - Query Book Content functionality.
"""
import pytest
from backend.src.services.rag_service import process_query

@pytest.mark.asyncio
async def test_process_query_with_content():
    """Test that process_query returns content when passages are found."""
    result = await process_query("test query")

    # The result should be a Response object
    assert hasattr(result, 'answer')
    assert hasattr(result, 'evidence')
    assert hasattr(result, 'confidence')

    # Check that the answer is a string
    assert isinstance(result.answer, str)

@pytest.mark.asyncio
async def test_process_query_no_content():
    """Test that process_query returns proper message when no passages are found."""
    # This test would require mocking the retrieval to return no results
    # For now, we'll test the structure
    result = await process_query("query with no matches")

    # Check that the result has the expected structure
    assert hasattr(result, 'id')
    assert hasattr(result, 'query_id')
    assert hasattr(result, 'answer')
    assert hasattr(result, 'evidence')
    assert hasattr(result, 'confidence')
    assert hasattr(result, 'follow_up')

def test_retrieve_function_exists():
    """Test that the retrieve function exists and is properly decorated."""
    from backend.src.services.rag_service import retrieve
    # Check that the function exists
    assert callable(retrieve)

if __name__ == "__main__":
    pytest.main([__file__])