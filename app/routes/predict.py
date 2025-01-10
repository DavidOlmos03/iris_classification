from fastapi import APIRouter
from app.schemas import IrisFeatures
from app.services.model_service import get_model_prediction

router = APIRouter()

@router.get("/info", tags=["Iris Prediction"],)
def read_root():
    """
        This endpoint returns a message indicating the purpose of the API.

    Returns:
        dict: A JSON object containing a message.
    """
    return {"message": "Welcome to the Iris classification API - Made by David Olmos"}


@router.post("/predict", tags=["Iris Prediction"],
        description=(
            "This endpoint performs the classification of the Iris flower "
            "according to its characteristics.\n"
        "1. Iris-Setosa\n"
        "2. Iris-Versicolour\n "
        "3. Iris-Virginica"
        ))
def predict(features: IrisFeatures):
    """
    This endpoint performs the classification of the Iris flower according to its characteristics.

    The endpoint takes a JSON object as input, which contains the features of the Iris flower.
    It then uses the trained model to make a prediction and returns the predicted class.

    Args:
        features (IrisFeatures): A JSON object containing the features of the Iris flower.

    Returns:
        dict: A JSON object containing the predicted class.
    """
    prediction = get_model_prediction(features)
    return {"class": prediction}
