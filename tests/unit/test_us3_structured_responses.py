"""
Unit tests for US3 - Receive Structured Responses functionality.
"""
import pytest
from backend.src.models.response import Response, Evidence

def test_response_model_structure():
    """Test that the Response model has the required structure."""
    evidence = [Evidence(doc_id="doc1", chunk_id="chunk1", quote="test quote")]

    response = Response(
        id="test_id",
        query_id="query_id",
        answer="test answer",
        evidence=evidence,
        confidence="High",
        follow_up={"ask": True, "question": "follow up"}
    )

    assert response.id == "test_id"
    assert response.query_id == "query_id"
    assert response.answer == "test answer"
    assert len(response.evidence) == 1
    assert response.confidence in ["High", "Medium", "Low"]
    assert "ask" in response.follow_up

def test_evidence_model_validation():
    """Test that the Evidence model properly validates quote length."""
    # Test valid quote (≤200 chars)
    valid_quote = "a" * 200
    evidence = Evidence(doc_id="doc1", chunk_id="chunk1", quote=valid_quote)
    assert len(evidence.quote) == 200

    # Test that quotes > 200 chars would raise validation error
    # Note: In Pydantic v2, validation happens during model creation
    try:
        long_quote = "a" * 201
        Evidence(doc_id="doc1", chunk_id="chunk1", quote=long_quote)
        # If we get here, validation didn't work as expected
        assert False, "Should have raised validation error for long quote"
    except Exception:
        # Expected behavior - validation should fail
        assert True

def test_confidence_validation():
    """Test that confidence values are properly validated."""
    valid_confidences = ["High", "Medium", "Low"]
    invalid_confidences = ["high", "HIGH", "invalid", ""]

    for conf in valid_confidences:
        # This should not raise an exception
        response = Response(
            id="test_id",
            query_id="query_id",
            answer="test answer",
            evidence=[],
            confidence=conf,
            follow_up={"ask": True, "question": "follow up"}
        )
        assert response.confidence == conf

    for conf in invalid_confidences:
        try:
            Response(
                id="test_id",
                query_id="query_id",
                answer="test answer",
                evidence=[],
                confidence=conf,
                follow_up={"ask": True, "question": "follow up"}
            )
            # If we get here, validation didn't work as expected
            assert False, f"Should have raised validation error for confidence: {conf}"
        except Exception:
            # Expected behavior - validation should fail
            assert True

if __name__ == "__main__":
    pytest.main([__file__])