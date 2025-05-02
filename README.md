# Proyecto final de MLOPS – Clasificador de flores iris

Este proyecto implementa un flujo completo de MLOps usando un modelo de clasificación simple basado en el dataset Iris de `sklearn`, como parte del curso de MLOps en LEAD University.

## Descripción del problema

Queremos poder clasificar automáticamente el tipo de flor (Setosa, Versicolor o Virginica) a partir de medidas del sépalo y del pétalo.

## Modelo utilizado

- `Modelo`: RandomForestClassifier
- `Dataset`: load_iris() de sklearn.datasets
- `Métrica principal`: accuracy_score

## Estructura del proyecto

- `retraining.py`: Script para reentrenar el modelo y guardar las métricas.
- `model/iris_model.pkl`: Modelo entrenado.
- `app.py`: Interfaz Streamlit para consumir el modelo desde una app web.
- `metrics.txt`: Accuracy del modelo.
- `Dockerfile`: Imagen para contenedor.
- `.github/workflows/main.yml`: Pipeline CI/CD con GitHub Actions.
- `requirements.txt`: Dependencias del proyecto.
- `README.md`: Documentación general.

## Instrucciones para correr localmente

**En la terminal**
git clone https://github.com/adriangonzalezp/mlops-iris.git  
cd mlops-iris  
python -m venv venv  
source venv/bin/activate  # o venv\Scripts\activate en Windows  
pip install -r requirements.txt  
python retraining.py  
streamlit run app.py  

## Aplicación desplegada en línea

http://3.148.224.163:8501

## Inputs y outputs esperados

**Inputs:**

Usar los sliders para elegir:

* Largo del sépalo (`sepal_length`)
* Ancho del sépalo (`sepal_width`)
* Largo del pétalo (`petal_length`)
* Ancho del pétalo (`petal_width`)

**Output:**

* Clase predicha (0, 1 o 2)

  * `0 = Setosa`
  * `1 = Versicolor`
  * `2 = Virginica`

## CI/CD y despliegue

* Reentrenamiento automático con GitHub Actions.
* Generación de métricas.
* Construcción de imagen Docker.
* Push de imagen a Docker Hub.
* Despliegue automático en instancia EC2 de AWS (puerto 8501).
* Pipeline definido en `.github/workflows/main.yml`.

## Consideraciones de seguridad

* Validación de entradas usando sliders en Streamlit.
* La llave `.pem` se usa como secreto en GitHub Actions (`EC2_PRIVATE_KEY`).
* El usuario, contraseña y host del servidor EC2 también se accesan como secretos de GitHub.

## Dataset utilizado

Este proyecto usa el dataset Iris de `sklearn.datasets`.

No se utilizó el dataset de cáncer de mama, cumpliendo con las restricciones del curso.

## Integrantes del equipo

* Adrián González – [@adriangonzalezp](https://github.com/adriangonzalezp)

## Branches utilizados

* `dev`: Rama de desarrollo.
* `main`: Rama estable para entregar.
