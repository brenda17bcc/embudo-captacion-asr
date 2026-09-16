import streamlit as st

# Configuración de la página (título de la pestaña, icono y ancho)
st.set_page_config(
    page_title="Ahorra en tus servicios",
    page_icon="💡",
    layout="centered"
)

# Cabecera: el "gancho" para que la persona quiera seguir
st.title("💡 ¿Estás pagando de más?")
st.subheader("Compara y ahorra en tus servicios del hogar")
st.write(
    "Déjanos tus datos y un asesor te preparará una propuesta "
    "**gratis y sin compromiso**."
)

# Lista de servicios que ofrece la asesora
SERVICIOS = [
    "🏥 Seguro médico",
    "🦷 Seguro dental",
    "🚗 Seguro de coche",
    "💡 Luz",
    "🌐 Internet",
    "📺 TV / Cable",
    "📱 Móvil",
    "🏠 Hipoteca",
]

# Paso 1 del embudo: elegir servicios
st.markdown("### Paso 1: ¿En qué te gustaría ahorrar?")
seleccion = st.multiselect("Elige uno o varios servicios", SERVICIOS)

# Mostrar lo elegido para comprobar que funciona
if seleccion:
    st.success(f"Has elegido: {', '.join(seleccion)}")