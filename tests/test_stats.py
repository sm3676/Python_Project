from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_stats_route():
    response = client.get("/stats")
    assert response.status_code in [200, 401]