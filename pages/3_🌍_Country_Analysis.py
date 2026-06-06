import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("🌍 Country Analysis")

df = load_data()

country_df = df.groupby("Country").agg({
    "Failure_Event_Count":"sum",
    "Maintenance_Cost":"mean"
}).reset_index()

fig = px.choropleth(
    country_df,
    locations="Country",
    locationmode="country names",
    color="Failure_Event_Count",
    hover_name="Country",
    title="Country Wise Failures"
)

st.plotly_chart(fig, use_container_width=True)
