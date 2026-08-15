"""Frontend Interactivo con Streamlit."""
import streamlit as st

st.set_page_config(page_title="Gestor de Productos", page_icon="📦")
st.title("📦 Panel de Control de Inventario")

nombre = st.text_input("Nombre del producto")
precio = st.number_input("Precio ($)", min_value=0.0, step=1.0)

if st.button("Guardar Producto"):
    st.success(f"Producto '{nombre}' guardado exitosamente.")
