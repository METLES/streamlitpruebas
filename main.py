import streamlit as st

# Título
st.title("El papu peres")

# Entrada de datos
st.header("1. El papu peres")
ingresos = st.number_input("¿Cuál es tu ingreso mensual después de impuestos?")
gastos = st.number_input("¿Cuáles son tus gastos mensuales fijos?")
deudas = st.number_input("¿Tienes deudas? Si es así, ¿cuánto debes?")
tasa_interes = st.number_input("¿A qué tasa de interés?")
metas = st.text_input("¿Cuáles son tus metas financieras?")
riesgo = st.slider("En una escala del 1 al 5, ¿cuál es tu tolerancia al riesgo?", 1, 5)

# Análisis y recomendaciones
if st.button("Obtener Recomendaciones"):
    st.header("2. Análisis y Recomendaciones")
    
    # Cálculos
    ahorro_mensual = ingresos - gastos
    perfil_riesgo = "Moderado" if riesgo == 3 else ("Conservador" if riesgo < 3 else "Agresivo")
    
    # Recomendaciones
    st.subheader("Recomendación de Inversión")
    st.write(f"Tu perfil de riesgo es {perfil_riesgo}. Te sugerimos invertir ${ahorro_mensual * 0.5:.2f} mensuales en un fondo indexado.")
    
    st.subheader("Gestión de Deudas")
    st.write(f"Te recomendamos pagar ${deudas * 0.05:.2f} adicionales mensuales para reducir tu deuda más rápido.")
    
    st.subheader("Planificación de Ahorros")
    st.write(f"Para alcanzar tu meta de {metas}, te sugerimos ahorrar ${ahorro_mensual * 0.3:.2f} mensuales en una cuenta de alto rendimiento.")
    
    st.subheader("Educación Financiera")
    st.write("Aquí tienes algunos recursos para aprender más:")
    st.write("- [Cómo diversificar tus inversiones](#)")
    st.write("- [Estrategias para pagar deudas](#)")
