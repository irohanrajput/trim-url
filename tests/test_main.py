import pytest
from fastapi.testclient import TestClient

from app.main import app

# Create test client
client = TestClient(app)

def test_root_endpoint():
    """Test that the root endpoint is accessible"""
    response = client.get("/")
    assert response.status_code == 200

def test_docs_endpoint():
    """Test that FastAPI docs are accessible"""
    response = client.get("/docs")
    assert response.status_code == 200

def test_openapi_endpoint():
    """Test that OpenAPI spec is accessible"""
    response = client.get("/openapi.json")
    assert response.status_code == 200

# Add your URL shortener specific tests here
# def test_create_short_url():
#     """Test creating a short URL"""
#     test_data = {"url": "https://example.com"}
#     response = client.post("/shorten", json=test_data)
#     assert response.status_code == 200
#     assert "short_url" in response.json()

# def test_redirect_short_url():
#     """Test redirecting from short URL"""
#     # First create a short URL
#     test_data = {"url": "https://example.com"}
#     create_response = client.post("/shorten", json=test_data)
#     short_code = create_response.json()["short_code"]
    
#     # Then test the redirect
#     redirect_response = client.get(f"/{short_code}", follow_redirects=False)
#     assert redirect_response.status_code == 307