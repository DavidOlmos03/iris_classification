"""
    This script trains and saves multiple models on the Iris dataset using MLflow.
"""

import logging
import joblib
import mlflow
import mlflow.sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def train_and_save_model(model_name, model):
    """
    Train a specified model on the Iris dataset and log the experiment with MLflow.

    Args:
        model_name (str): Name of the model (e.g., 'DecisionTree', 'RandomForest', 'SVC').
        model (Any): The model instance to train.

    Returns:
        None: Logs the metrics, parameters, and model to MLflow.
    """
    # Load the dataset
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target

    # Divide the dataset into training and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    with mlflow.start_run(run_name=model_name):
        # Train the model
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, predictions)

        # Log parameters, metrics, and model
        mlflow.log_param("model_name", model_name)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, artifact_path=model_name)

        # Save the model locally
        model_file = f"{model_name}.pkl"
        joblib.dump(model, model_file)
        mlflow.log_artifact(model_file)

        logging.info(f"Model {model_name} saved to file {model_file} with accuracy {accuracy:.4f}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Define models to test
    models = {
        "DecisionTree": DecisionTreeClassifier(),
        "RandomForest": RandomForestClassifier(),
        "SVC": SVC()
    }

    for model_name, model in models.items():
        train_and_save_model(model_name, model)

    logging.info("All models trained and logged with MLflow.")
