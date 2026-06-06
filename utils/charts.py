import plotly.express as px

def maintenance_cost_chart(df):

    chart = px.bar(
        df.groupby("Device_Type")["Maintenance_Cost"]
        .mean()
        .reset_index(),
        x="Device_Type",
        y="Maintenance_Cost",
        color="Device_Type",
        title="Average Maintenance Cost"
    )

    return chart


def country_chart(df):

    chart = px.pie(
        df,
        names="Country",
        title="Country Distribution"
    )

    return chart
