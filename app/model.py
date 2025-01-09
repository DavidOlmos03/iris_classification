import joblib
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import os

def train_and_save_model():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar el modelo
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    print("Directorio actual:", os.getcwd())


    # Guardar el modelo entrenado
    joblib.dump(clf, "model.pkl")

def load_model():
    print("Directorio actual para load:", os.getcwd())
    return joblib.load("model.pkl")

