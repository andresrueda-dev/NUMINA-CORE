import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="NUMINA CORE",
    layout="wide"
)

st.title("🧠 NUMINA CORE")
st.subheader("Pattern & Anomaly Detection Engine")

# métricas
col1, col2, col3 = st.columns(3)

col1.metric("Tickets Analizados", "1,284")
col2.metric("Patrones Detectados", "37")
col3.metric("Anomalías", "5")

st.divider()

# tabla ejemplo
data = pd.DataFrame({
    "ID": [101,102,103,104],
    "Score": [87,23,91,45],
    "Estado": ["Normal","Anómalo","Normal","Riesgo"]
})

st.dataframe(data)

st.divider()

# gráfica simple
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

st.line_chart(chart_data)

st.success("Sistema NUMINA operativo")
