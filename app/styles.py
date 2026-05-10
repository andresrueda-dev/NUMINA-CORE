import streamlit as st

def load_styles():

    st.markdown(
        '''
        <style>

        .stApp {
            background-color: #111827;
            color: #F9FAFB;
        }

        h1,h2,h3 {
            color: #0A84FF;
        }

        </style>
        ''',
        unsafe_allow_html=True
    )
