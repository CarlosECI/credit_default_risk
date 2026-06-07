import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title('Detector de Riesgo Crediticio')
st.markdown('Introduce los datos del solicitante para evaluar el riesgo de impago')

model = joblib.load('../Models/lgbm_model.pkl')
scaler = joblib.load('../Models/scaler.pkl')

