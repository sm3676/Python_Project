from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_history_route():
    response = client.get("/history")
    assert response.status_code in [200, 401]