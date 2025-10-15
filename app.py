import streamlit as st 
import math
import matplotlib

st.title("Mi Aplicación para Calcular Figuras y Relaciones Trigonométricas en Streamlit 🖩")

# Selección de figura
figura = st.selectbox("Selecciona una figura geometrica", ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"])

# Círculo
if figura == "Círculo":
    radio = st.slider("Selecciona el radio", 0.0, 20.0, 5.0)
# calculo del area
    area = math.pi * radio**2
#calculo del perimetro
    perimetro = 2 * math.pi * radio
# resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")
# Imagen de la figura
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radio, color=color, fill=False)
    ax.add_artist(circle)
    ax.set_aspect('equal')
    st.pyplot(fig)

# Triángulo
elif figura == "Triángulo":
    base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
    lado_a = st.slider("Lado a", 0.0, 20.0, 5.0)
    lado_b = st.slider("Lado b", 0.0, 20.0, 5.0)
    lado_c = st.slider("Lado c", 0.0, 20.0, 5.0)
# calculo del area
    area = 0.5 * base * altura
# calculo del perimetro
    perimetro = lado_a + lado_b + lado_c
#resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Rectángulo
elif figura == "Rectángulo":
    base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
# calculo del area
    area = base * altura
# calculo del perimetro
    perimetro = 2 * (base + altura)
# calculos
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Cuadrado
elif figura == "Cuadrado":
    lado = st.slider("Selecciona el lado", 0.0, 20.0, 5.0)
# calculo del area
    area = lado**2
# calculo del perimetro
    perimetro = 4 * lado
# resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")


