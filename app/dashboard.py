import streamlit as st
import pandas as pd

def show_dashboard(df):

    st.subheader("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.line_chart(df.select_dtypes("number"))
