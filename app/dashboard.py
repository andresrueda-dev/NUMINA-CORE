import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from engine.pattern_analyzer import analyze_patterns

def show_dashboard(df):

    st.subheader("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Pattern Frequency")

    patterns = analyze_patterns(df)

    pattern_df = pd.DataFrame(
        patterns,
        columns=["Number", "Frequency"]
    )

    st.dataframe(
        pattern_df,
        use_container_width=True
    )

    st.bar_chart(
        pattern_df.set_index("Number")
    )
