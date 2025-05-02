# Proyecto final de MLOPS LEAD University – Clasificador de flores iris

En este proyecto se implementa un flujo de MLOPS usando un modelo de clasificación bastante simple basado en el dataset Iris que trae por defecto la librería sklearn.


## Descripción del problema

Queremos poder clasificar automáticamente el tipo de flor (Setosa, Versicolor o Virginica) a partir de medidas de sépalo y pétalo.


## Estructura del proyecto

- retraining.py: Un script para reentrenar el modelo y guardar las métricas.
- model/iris_model.pkl: Modelo ya entrenado.
- app.py: UI de Streamlit para consumir el modelo.
- metrics.txt: Archivo generado con el accuracy del modelo.
- Dockerfile: Para definir la imagen donde se se despliega la app.
- .github/workflows/main.yml: Pipeline CI/CD usando GitHub Actions.


## Instrucciones para correr localmente

**En la terminal:**

git clone https://github.com/adriangonzalezp/mlops-iris.git  
cd mlops-iris  
python -m venv venv  
source venv/bin/activate  # o venv\Scripts\activate en Windows  
pip install -r requirements.txt  
python retraining.py  
streamlit run app.py  
