import streamlit as st
import pandas as pd
from engine.core_engine import scan_ticket, detect_anomalies, analyze_patterns

st.set_page_config(page_title="NUMINA CORE", layout="wide")

st.title("NUMINA CORE")
st.caption("Pattern & Anomaly Detection Engine")

uploaded = st.file_uploader("Upload tickets (.txt or .csv)", type=["txt", "csv"])

if uploaded:
    content = uploaded.read().decode("utf-8")
    lines = content.splitlines()

    results = []

    for line in lines:
        scan = scan_ticket(line)
        anomalies, score = detect_anomalies(scan)
        patterns = analyze_patterns(scan)

        results.append({
            "ticket": line,
            "length": scan["length"],
            "score": score,
            "anomalies": ", ".join(anomalies)
        })

    df = pd.DataFrame(results)

    st.subheader("📊 Analysis Table")
    st.dataframe(df)

    st.subheader("🔥 Anomaly Score Distribution")
    st.bar_chart(df["score"])

    st.subheader("🚨 High Risk Tickets")
    high = df[df["score"] > 40]
    st.dataframe(high)
