import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuración de la página ---
st.set_page_config(
    page_title="AutoInsights Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 AutoInsights Dashboard")
st.markdown("""
Este dashboard te permite explorar datos reales de anuncios de ventas de vehículos en EE.UU.
Usa los controles para generar visualizaciones interactivas.
""")

# --- Cargar datos ---
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

car_data = load_data()

st.sidebar.header("Opciones de Visualización")
st.sidebar.markdown("Selecciona qué gráficos quieres generar.")

# --- Histograma ---
if st.sidebar.checkbox("Mostrar Histograma (Odometer)", value=True):
    st.subheader("Distribución del Odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico de Dispersión ---
if st.sidebar.checkbox("Mostrar Dispersión (Odometer vs Price)", value=True):
    st.subheader("Relación entre Odómetro y Precio")
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.caption("Desarrollado por Alexander  Herrera — Proyecto educativo para análisis de datos.")
