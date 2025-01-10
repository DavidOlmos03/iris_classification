from fastapi import APIRouter
from app.schemas import IrisFeatures
from app.services.model_service import get_model_prediction

router = APIRouter()

@router.get("/info", tags=["Iris Prediction"],)
def read_root():
    return {"message": "Welcome to the Iris classification API - Made by David Olmos"}


@router.post("/predict", tags=["Iris Prediction"],
        description="This endpoint performs the classification of the Iris flower according to its characteristics.\n"
        "1. Iris-Setosa\n"
        "2. Iris-Versicolour\n "
        "3. Iris-Virginica")
def predict(features: IrisFeatures):
    prediction = get_model_prediction(features)
    return {"class": prediction}
    
