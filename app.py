
import streamlit as st

st.set_page_config(
    page_title="Medical Device Analytics",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Medical Device Failure Analytics Dashboard")

st.markdown("""
Welcome to the advanced healthcare analytics dashboard.

Use the sidebar to navigate between pages.
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", "4000+")
col2.metric("Countries", "20+")
col3.metric("Manufacturers", "15+")
col4.metric("Analytics", "Deep Insights")

st.image("assets/banner.png", use_container_width=True)

st.success("Project Loaded Successfully ✅")
