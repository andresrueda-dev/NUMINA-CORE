import streamlit as st
import pandas as pd

def upload_dataset():

    uploaded = st.file_uploader(
        "Upload CSV Dataset",
        type=["csv"]
    )

    if uploaded:

        df = pd.read_csv(uploaded)

        return df

    return None
