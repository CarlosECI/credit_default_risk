import streamlit as st
import pandas as pd
import numpy as np
import joblib
from src.data_processing import clean_column_name

st.title('Detector de Riesgo Crediticio')
st.markdown('Introduce los datos del solicitante para evaluar el riesgo de impago')


@st.cache_resource
def load_model():
    model = joblib.load('./Models/lgbm_model.pkl')
    scaler = joblib.load('./Models/scaler.pkl')
    features = joblib.load('./Models/feature_columns.pkl')
    imputation_values = joblib.load('./Models/imputation_values.pkl')
    
    return model, scaler, features, imputation_values

model, scaler, features, imputation_values = load_model()

col1, col2 = st.columns(2)

with col1:
    edad = st.number_input('Edad', min_value=21, max_value=69, value='min')
    genero = st.selectbox('Género', ['F', 'M'])
    tipo_ingreso = st.selectbox('Tipo de ingreso', ['Working',
    'State servant',
    'Commercial associate',
    'Pensioner',
    'Unemployed',
    'Student',
    'Maternity leave',
    'Businessman'])
    salario = st.number_input('Salario mensual', min_value=1)
    ant_laboral = st.slider('Antiguedad laboral en meses', 0, 150, 18)
    
with col2:
    tipo_educacion = st.selectbox('Nivel educativo', ['Academic degree','Secondary / secondary special',
    'Higher education',
    'Incomplete higher',
    'Lower secondary'])
    credito = st.number_input('Monto del crédito', min_value=100)
    precio_bien = st.number_input('Precio del bien a financiar', min_value=100)
    creditos_activos = st.number_input('Número de créditos activos', min_value=0)
    cuota_credito = st.number_input('Gasto mensual en creditos activos', min_value=0)

df = pd.DataFrame([[0]*len(features)], columns=features)

df['AMT_INCOME_TOTAL'] = salario * 12
df['AMT_INCOME_TOTAL_LOG'] = np.log(salario * 12)
df['DAYS_BIRTH'] = edad * -365
df['AGE_YEARS'] = edad
df['DAYS_EMPLOYED'] = ant_laboral * -30
df['AMT_CREDIT'] = credito
df['AMT_GOODS_PRICE'] = precio_bien
df['ratio_credito_valor'] = credito / precio_bien
df['creditos_activos'] = creditos_activos
df['CODE_GENDER_M'] = int(genero == 'M')
df['ratio_deuda_ingreso'] = df['AMT_CREDIT'] / df['AMT_INCOME_TOTAL']
df['AMT_ANNUITY'] = cuota_credito * 12
df['ratio_anuidad_ingreso'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
df['ratio_antiguedad_empleo'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']
df['docs_entregados'] = imputation_values['docs_entregados']
col_income = f'NAME_INCOME_TYPE_{clean_column_name(tipo_ingreso)}'
if col_income in features:
    df[col_income] = 1
col_education = f'NAME_EDUCATION_TYPE_{clean_column_name(tipo_educacion)}'
if col_education in features:
    df[col_education] = 1

def prediction(df):
    data = scaler.transform(df)
    data = pd.DataFrame(data, columns=features)
    
    result = model.predict_proba(data)[:, 1]
    
    return result

if st.button('Evaluar riesgo'):
    resultado = prediction(df)
    st.write(f'Probabilidad de impago: {resultado[0]:.2%}')
    
    if resultado < 0.30:
        st.success('Riesgo bajo de impago, se puede asignar el crédito')
    elif resultado < 0.65:
        st.warning('Riesgo moderado de impago, se recomienda solicitar fiador de respaldo')
    else:
        st.warning('Riesgo muy alto de impago, no se recomienda asignar el crédito')