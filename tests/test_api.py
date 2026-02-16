from fastapi.testclient import TestClient
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from backend.main import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200

def test_rank():
    response = client.post(
        "/rank",
        json={"job_description": "Python SQL Power BI"}
    )
    assert response.status_code == 200
    assert "ranking" in response.json()
