from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_prediction():

    payload = {
        "Glucose": 120,
        "BloodPressure": 70,
        "BMI": 25.5,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 30
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "result" in data
    assert "probability" in data