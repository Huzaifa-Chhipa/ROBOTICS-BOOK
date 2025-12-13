"""
Integration tests for US1 - Query Book Content functionality.
"""
import pytest
from backend.src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_query_endpoint_exists():
    """Test that the query endpoint is available."""
    # This is a basic test to check the endpoint exists
    # In a real implementation, we would test the actual functionality
    # but this requires a working Qdrant instance and API keys
    assert hasattr(app, 'routes')

    # Find the query route
    query_route_exists = False
    for route in app.routes:
        if hasattr(route, 'path') and route.path == '/api/v1/query':
            query_route_exists = True
            break

    assert query_route_exists, "Query endpoint should exist"

def test_health_endpoint():
    """Test the health endpoint."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    data = response.json()
    assert "status" in data
    assert "timestamp" in data
    assert "dependencies" in data

if __name__ == "__main__":
    pytest.main([__file__])