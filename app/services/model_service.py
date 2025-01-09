import numpy as np
from app.model import load_model, train_and_save_model
from app.schemas import IrisFeatures


# Load model, only once at startup app
train_and_save_model()
model = load_model()

def get_model_prediction(features: IrisFeatures) -> int:
    # Convert features into a numpy array for prediction
    data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    prediction = model.predict(data)
    return int(prediction[0])
