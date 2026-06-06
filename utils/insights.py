def generate_insights(df):

    highest_cost = df.groupby(
        "Device_Type"
    )["Maintenance_Cost"].mean().idxmax()

    highest_failure = df.groupby(
        "Manufacturer"
    )["Failure_Event_Count"].sum().idxmax()

    insights = f"""
    Highest maintenance cost device:
    {highest_cost}

    Manufacturer with highest failures:
    {highest_failure}
    """

    return insights
