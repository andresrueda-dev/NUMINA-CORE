import streamlit as st

st.set_page_config(page_title="NUMINA CORE", layout="wide")

st.title("NUMINA CORE")
st.caption("Pattern & Anomaly Detection Engine")

file = st.file_uploader("Upload ticket", type=["txt", "csv"])

if file:
    content = file.read().decode("utf-8")
    st.success("File loaded")
    st.text(content)
