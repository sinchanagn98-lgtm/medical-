import streamlit as st

# Page Config
st.set_page_config(
    page_title="Medical Device Analytics",
    page_icon="🏥",
    layout="wide"
)

# Load CSS
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Banner
st.markdown("""
<div style="
    background: linear-gradient(90deg,#0f172a,#1e40af);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
">

<h1>🏥 Medical Device Failure Analytics</h1>

<h3>Advanced Healthcare Monitoring Dashboard</h3>

<p>
📊 Deep Analytics |
🌍 Global Insights |
⚠️ Failure Prediction |
🧠 Smart Monitoring
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", "4000+")
col2.metric("Countries", "20+")
col3.metric("Manufacturers", "15+")
col4.metric("Analytics", "Deep Insights")

st.divider()

st.success("Dashboard Loaded Successfully ✅")
