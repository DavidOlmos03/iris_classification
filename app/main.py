from fastapi import FastAPI
from app.model import load_model
from app.schemas import IrisFeatures
import numpy as np

app = FastAPI()

# Cargar el modelo entrenado al iniciar la aplicación
model = load_model()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de clasificación del Iris"}

@app.post("/predict")
def predict(features: IrisFeatures):
    data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    prediction = model.predict(data)
    return {"class": int(prediction[0])}

