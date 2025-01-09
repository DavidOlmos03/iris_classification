import joblib
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def train_and_save_model():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Divide the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the decision tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)



    # Save the trained model to a file .pkl
    joblib.dump(clf, "model.pkl")
    print("Model saved to file model.pkl")

def load_model():
    print("Model loaded from file model.pkl")
    return joblib.load("model.pkl")


