# app/streamlit_app.py
import streamlit as st
import numpy as np
import joblib

st.title("🎬 Recomendador de Gênero de Filme por Personalidade")

model = joblib.load("app/model.pkl")
labels = joblib.load("app/labels.pkl")

criatividade = st.slider("Criatividade", 0.0, 1.0, 0.5)
extroversao = st.slider("Extroversão", 0.0, 1.0, 0.5)
racionalidade = st.slider("Racionalidade", 0.0, 1.0, 0.5)

if st.button("Recomendar gênero"):
    features = np.array([[criatividade, extroversao, racionalidade]])
    pred = model.predict(features)[0]
    genero = labels[pred]
    st.success(f"🎥 Gênero recomendado: **{genero}**")
