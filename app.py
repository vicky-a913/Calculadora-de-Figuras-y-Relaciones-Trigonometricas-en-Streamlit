import streamlit as st 
import math

st.title("Mi Aplicación para Calcular Figuras y Relaciones Trigonométricas en Streamlit 🖩")

# Selección de figura
figura = st.selectbox("Selecciona una figura geométrica",["Círculo"])

# Widget para ingresar el radio
radio = st.slider("Selecciona el radio", 0.0, 10.0, 5.0)

# Cálculo de área
area = math.pi * radio**2

# Cálculo del perimetro
perimetro = 2 * math.pi * radio

# Mostrar resultado
st.write(f"El área del círculo con radio {radio} es:{area:2f}")

# Selección de figura
figura = st.selectbox("Selecciona una figura geométrica",["Triángulo"])

# Widget para ingresar el area
area = st.slider("Seleccionar el area", 0.0, 10.0, 5.0)

if figura == "Triangulo"
    base = st.slider("Selecciona la base", 0.0, 10.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 10.0, 5.0)
    lado_a = st.slider("Lado a", 0.0, 10.0, 5.0)
    lado_b = st.slider("Lado b", 0.0, 10.0, 5.0)
    lado_c = st.slider("Lado c", 0.0, 10.0, 5.0)
    area = 0.5 * base * altura
    perimetro = lado_a + lado_b + lado_c
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")
