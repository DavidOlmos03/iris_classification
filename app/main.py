from fastapi import FastAPI
from app.routes.predict import router as predict_router

app = FastAPI(
    title="Iris Classification API",
    description=("This API performs the classification of the Iris flower species"
    "based on its features."
    ),
    version="1.0.0"
)

# Include the prediction routes
app.include_router(predict_router)
