import streamlit as st

from app.upload import upload_dataset
from app.dashboard import show_dashboard

st.set_page_config(
    page_title="NUMINA CORE",
    layout="wide"
)

st.title("NUMINA CORE")

df = upload_dataset()

if df is not None:

    show_dashboard(df)

else:

    st.info("Upload a dataset")
