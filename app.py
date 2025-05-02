import streamlit as st
import joblib
import numpy as np

# apcicacion simple con streamlit
st.title("Clasificador de flores Iris")

model = joblib.load("model/iris_model.pkl")

sepal_length = st.slider("Sepal length", 4.0, 8.0)
sepal_width = st.slider("Sepal width", 2.0, 4.5)
petal_length = st.slider("Petal length", 1.0, 7.0)
petal_width = st.slider("Petal width", 0.1, 2.5)

features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(features)

st.write(f"Predicción: **{prediction[0]}**")