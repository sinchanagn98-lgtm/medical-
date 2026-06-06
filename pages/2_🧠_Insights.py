import streamlit as st
from utils.data_loader import load_data
from utils.insights import generate_insights

st.title("🧠 Smart Insights")

df = load_data()

insights = generate_insights(df)

st.success(insights)

st.markdown("## 📌 AI Generated Observations")

st.write("""
- Preventive maintenance reduces failures.
- Some manufacturers show higher downtime.
- Devices with high maintenance cost tend to fail more.
- Downtime increases operational risk.
""")
