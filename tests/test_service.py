from src.service import app
from fastapi.testclient import TestClient

def test_import_app():
    assert app is not None

def test_health_check():
    client = TestClient(app)
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}