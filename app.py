import streamlit as st 
import math

st.title("Mi Aplicación para Calcular Figuras y Relaciones Trigonométricas en Streamlit 🖩")

# Selección de figura
figura = st.selectbox("Selecciona una figura geométrica",["Círculo"])

# Widget para ingresar el radio
radio = st.slider("Selecciona el radio", 0.0, 10.0, 5.0)

# Cálculo de área
area = math.pi * radio**2

# Mostrar resultado
st.write(f"El área del círculo con radio {radio} es:{area:2f}")
