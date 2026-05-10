import streamlit as st

from app.styles import load_styles
from app.visualizer import show_header
from app.upload import upload_dataset
from app.dashboard import show_dashboard

st.set_page_config(
    page_title="NUMINA CORE",
    layout="wide"
)

load_styles()

show_header()

st.markdown("---")

df = upload_dataset()

if df is not None:

    show_dashboard(df)

else:

    st.info(
        "Upload a dataset to begin analysis"
    )
