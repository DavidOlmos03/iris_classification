# Iris Classification API

Esta API utiliza un modelo de clasificación para predecir las clases del conjunto de datos Iris.

This API uses a classification model to predict the classes of the Iris dataset.

## Endpoints

### GET `/info`
- Responde con un mensaje de bienvenida./Returns a welcome message.

### POST `/predict`
- **Descripción/Description**: Predice la clase del Iris con base en las características de entrada./ Predicts the class of the Iris based on the input features.

- **Formato de entrada/Input format** (JSON):
  ```json
  {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }

## Iniciar el proyecto/Start the project

1. Clonar el repositorio / Clone the repository

  ```bash
  git clone https://github.com/davidam/iris_classification.git
  ```

2. Entrar al directorio del proyecto / Enter the project directory

  ```bash
  cd iris_classification
  ```

3. Contruir la imagen Docker / Build the Docker image

  ```bash
  docker build -t iris_classification .
  ```
4. Ejecutar el contenedor Docker / Run the Docker container 

  ```bash
  docker run -p 8000:8000 iris_classification
  ```
5. Acceder a la API / Access the API

  Abre tu navegador web e ingresa a la URL/Start your web browser and enter the URL 
  ```bash
  http://localhost:8000/docs
  ```
  or
  ```bash
  http://localhost:8000/redoc
  ```