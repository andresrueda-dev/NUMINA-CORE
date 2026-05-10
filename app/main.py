import streamlit as st

from styles import load_styles
from visualizer import show_header
from upload import upload_dataset
from dashboard import show_dashboard

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
