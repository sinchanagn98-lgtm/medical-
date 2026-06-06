
import streamlit as st
import plotly.express as px
from utils.data_loader import load_data
from utils.charts import maintenance_cost_chart
from utils.charts import country_chart

st.title("📊 Deep Analytics Dashboard")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

device = st.sidebar.multiselect(
    "Select Device Type",
    df["Device_Type"].unique(),
    default=df["Device_Type"].unique()
)

manufacturer = st.sidebar.multiselect(
    "Select Manufacturer",
    df["Manufacturer"].unique(),
    default=df["Manufacturer"].unique()
)

filtered_df = df[
    (df["Device_Type"].isin(device)) &
    (df["Manufacturer"].isin(manufacturer))
]

# KPI Cards
st.subheader("📌 Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Devices",
    len(filtered_df)
)

c2.metric(
    "Avg Cost",
    f"${filtered_df['Maintenance_Cost'].mean():.0f}"
)

c3.metric(
    "Avg Downtime",
    f"{filtered_df['Downtime'].mean():.2f} hrs"
)

c4.metric(
    "Failures",
    int(filtered_df['Failure_Event_Count'].sum())
)

st.divider()

# Charts
chart1 = maintenance_cost_chart(filtered_df)
st.plotly_chart(chart1, use_container_width=True)

chart2 = country_chart(filtered_df)
st.plotly_chart(chart2, use_container_width=True)

# Scatter Plot
scatter = px.scatter(
    filtered_df,
    x="Failure_Event_Count",
    y="Downtime",
    color="Device_Type",
    size="Maintenance_Cost",
    hover_data=["Manufacturer"],
    title="Failure Events vs Downtime"
)

st.plotly_chart(scatter, use_container_width=True)

# Heatmap
numeric_df = filtered_df.select_dtypes(include="number")

corr = numeric_df.corr()

heatmap = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Heatmap"
)

st.plotly_chart(heatmap, use_container_width=True)
