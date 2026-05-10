import streamlit as st
import pandas as pd
import numpy as np

# =========================================
# CONFIGURACIÓN GENERAL
# =========================================

st.set_page_config(
    page_title="NUMINA CORE",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:
    st.title("🧠 NUMINA CORE")

    st.markdown("---")

    module = st.selectbox(
        "Selecciona módulo",
        [
            "Dashboard",
            "Data Explorer",
            "Pattern Analysis",
            "Anomaly Detection",
            "Statistics Lab"
        ]
    )

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Carga un archivo CSV",
        type=["csv"]
    )

# =========================================
# DATOS
# =========================================

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

else:
    # DATASET DEMO
    np.random.seed(42)

    df = pd.DataFrame({
        "Ticket": np.arange(1000, 1100),
        "Score": np.random.randint(1, 100, 100),
        "Category": np.random.choice(
            ["Normal", "Risk", "Critical"],
            100
        ),
        "Pattern": np.random.choice(
            ["A", "B", "C", "D"],
            100
        )
    })

# =========================================
# HEADER
# =========================================

st.title("🧠 NUMINA CORE")
st.caption("Pattern & Anomaly Detection Engine")

st.markdown("---")

# =========================================
# DASHBOARD
# =========================================

if module == "Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Records",
        len(df)
    )

    col2.metric(
        "Average Score",
        round(df["Score"].mean(), 2)
    )

    col3.metric(
        "Max Score",
        df["Score"].max()
    )

    anomalies = len(df[df["Score"] > 80])

    col4.metric(
        "Potential Anomalies",
        anomalies
    )

    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.subheader("Score Evolution")
        st.line_chart(df["Score"])

    with right:
        st.subheader("Category Distribution")
        st.bar_chart(df["Category"].value_counts())

    st.markdown("---")

    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

# =========================================
# DATA EXPLORER
# =========================================

elif module == "Data Explorer":

    st.subheader("Data Explorer")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Dataset Information")

    info = pd.DataFrame({
        "Column": df.columns,
        "Type": [str(dtype) for dtype in df.dtypes]
    })

    st.table(info)

# =========================================
# PATTERN ANALYSIS
# =========================================

elif module == "Pattern Analysis":

    st.subheader("Pattern Frequency")

    pattern_counts = df["Pattern"].value_counts()

    st.bar_chart(pattern_counts)

    st.markdown("---")

    st.subheader("Pattern Table")

    st.dataframe(
        pattern_counts.reset_index(),
        use_container_width=True
    )

# =========================================
# ANOMALY DETECTION
# =========================================

elif module == "Anomaly Detection":

    st.subheader("Anomaly Detection Engine")

    threshold = st.slider(
        "Anomaly Threshold",
        1,
        100,
        80
    )

    df["Anomaly"] = df["Score"] > threshold

    anomalies_df = df[df["Anomaly"] == True]

    col1, col2 = st.columns(2)

    col1.metric(
        "Detected Anomalies",
        len(anomalies_df)
    )

    percentage = (
        len(anomalies_df) / len(df)
    ) * 100

    col2.metric(
        "Anomaly %",
        f"{percentage:.2f}%"
    )

    st.markdown("---")

    st.dataframe(
        anomalies_df,
        use_container_width=True
    )

# =========================================
# STATISTICS LAB
# =========================================

elif module == "Statistics Lab":

    st.subheader("Statistical Analysis")

    st.write(df.describe())

    st.markdown("---")

    st.subheader("Correlation Matrix")

    numeric_df = df.select_dtypes(
        include=np.number
    )

    st.dataframe(
        numeric_df.corr(),
        use_container_width=True
    )

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.success("NUMINA CORE ONLINE")
