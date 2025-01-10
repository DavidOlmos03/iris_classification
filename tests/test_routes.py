"""
    This module contains tests for the routes.py file.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_info_endpoint():
    """
        Test that the info endpoint returns the expected message.
    """
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Iris classification API - Made by David Olmos"}

def test_predict_valid_input():
    """
        Test that the predict endpoint returns the expected response.
    """
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "class" in response.json()

def test_predict_invalid_input():
    """
        Test that the predict endpoint returns the expected error.
    """
    payload = {
        "sepal_length": -5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": "invalid"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
