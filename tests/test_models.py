"""
    This module contains tests for the model.py file.
"""

import os
import pytest
from app.services.model_service import train_and_save_model, load_model

def test_train_and_save_model():
    """
        Test that the model is trained and saved correctly.
    """
    train_and_save_model()
    assert os.path.exists("model.pkl"), "Model file was not saved."

def test_load_model():
    """
        Test that the model is loaded correctly.
    """
    model = load_model()
    assert model is not None, "Model could not be loaded."

def test_model_prediction():
    """
        Test that the model makes the correct prediction.
    """
    model = load_model()
    input_data = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(input_data)
    assert prediction[0] in [0, 1, 2], "Prediction is not in expected class range."
