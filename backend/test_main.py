import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is my Api for the sentiment analysis"}

def test_positive_predict():
    response = client.post("/model", json = {"text":"This is the best day of my life"})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "This is the best day of my life"
    assert data["sentiment"] == "Positive"
    assert type(data["sentiment_val"]) == float

def test_negative_predict():
    response = client.post("/model", json = {"text":"I hate this, this is the worst."})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "I hate this, this is the worst."
    assert data["sentiment"] == "Negative"
    assert type(data["sentiment_val"]) == float
