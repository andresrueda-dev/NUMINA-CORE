import streamlit as st
from config.settings import *

def load_styles():

    st.markdown(f'''
    <style>

    .stApp {{
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR};
    }}

    h1,h2,h3 {{
        color: {PRIMARY_COLOR};
    }}

    </style>
    ''', unsafe_allow_html=True)
