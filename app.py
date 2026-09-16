import re
import streamlit as st
from database import crear_tabla, guardar_contacto

# ---------- CONFIGURACIÓN ----------
st.set_page_config(
    page_title="Ahorra en tus servicios",
    page_icon="💡",
    layout="centered"
)
crear_tabla()

# ---------- CABECERA ----------
st.title("💡 ¿Estás pagando de más?")
st.subheader("Compara y ahorra en tus servicios del hogar")
st.write(
    "Déjanos tus datos y un asesor te preparará una propuesta "
    "**gratis y sin compromiso**."
)

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

# ---------- PASO 1: SERVICIOS ----------
st.markdown("### Paso 1: ¿En qué te gustaría ahorrar?")
seleccion = st.multiselect("Elige uno o varios servicios", SERVICIOS)

if not seleccion:
    st.info("👆 Elige al menos un servicio para continuar.")
    st.stop()

# ---------- PASO 2: CUÁNTO PAGA ----------
st.markdown("### Paso 2: ¿Cuánto pagas ahora al mes?")
st.caption("Un valor aproximado es suficiente. Si no lo sabes, déjalo en 0.")

pagos = {}
for servicio in seleccion:
    pagos[servicio] = st.number_input(
        f"{servicio} (€/mes)",
        min_value=0.0,
        step=5.0,
        key=f"pago_{servicio}"
    )

total_mensual = sum(pagos.values())
if total_mensual > 0:
    st.info(
        f"Ahora pagas unos **{total_mensual:.2f} € al mes** "
        f"(**{total_mensual * 12:.0f} € al año**). ¡Veamos si podemos reducirlo!"
    )

# ---------- PASO 3: DATOS DE CONTACTO ----------
st.markdown("### Paso 3: ¿Dónde te enviamos tu propuesta?")

with st.form("formulario_contacto"):
    nombre = st.text_input("Nombre *")
    telefono = st.text_input("Teléfono / WhatsApp *")
    email = st.text_input("Email (opcional)")
    ciudad = st.text_input("Ciudad o código postal")
    horario = st.selectbox(
        "¿Cuándo prefieres que te contactemos?",
        ["Indiferente", "Mañana", "Tarde"]
    )
    acepta = st.checkbox(
        "Acepto que mis datos se usen para contactarme "
        "con una propuesta personalizada *"
    )
    enviado = st.form_submit_button("💰 Quiero mi propuesta gratis")

# ---------- VALIDACIÓN ----------
if enviado:
    errores = []

    if not nombre.strip():
        errores.append("Escribe tu nombre.")

    telefono_limpio = re.sub(r"[\s\-]", "", telefono)
    if not re.fullmatch(r"\+?\d{9,15}", telefono_limpio):
        errores.append("Escribe un teléfono válido (mínimo 9 dígitos).")

    if email.strip() and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
        errores.append("El email no parece válido.")

    if not acepta:
        errores.append("Debes aceptar el uso de tus datos para que podamos contactarte.")

    if errores:
        for error in errores:
            st.error(error)
    else:
        guardar_contacto(
            nombre=nombre.strip(),
            telefono=telefono_limpio,
            email=email.strip(),
            ciudad=ciudad.strip(),
            horario=horario,
            pagos=pagos,
            consentimiento=acepta,
        )
        st.success(
            f"¡Gracias, {nombre.strip()}! 🎉 "
            "Un asesor te contactará pronto con tu propuesta."
        )
        st.balloons()