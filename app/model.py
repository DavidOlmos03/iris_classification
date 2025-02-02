"""
    Module to train and save the model, also to load the model.
"""

import joblib
import logging
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def train_and_save_model():
    """
    Train a Support Vector Classifier on the Iris dataset and save the trained model to a file.

    The function performs the following steps:
    1. Loads the Iris dataset.
    2. Splits the data into training and testing sets.
    3. Trains a Support Vector Classifier on the training data.
    4. Saves the trained model to a file named 'model.pkl'.

    Returns:
        None: This function does not return a value. It saves the trained model to a file.
    """
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target

    # Divide the dataset into training and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Create and train the Support Vector Classifier
    clf = SVC()
    clf.fit(x_train, y_train)

    # Save the trained model to a file .pkl
    joblib.dump(clf, "model.pkl")
    logging.info('Model saved to file model.pkl')

def load_model():
    """
    Load the trained model from the file 'model.pkl'.

    Returns:
        Any: The model loaded from the file 'model.pkl'.
    """
    logging.info('Model loaded from file model.pkl')
    return joblib.load("model.pkl")
