import streamlit as st
import random

st.title("⚠️ Failure Prediction System")

st.subheader("Enter Device Information")

maintenance_cost = st.number_input(
    "Maintenance Cost"
)

downtime = st.number_input(
    "Downtime"
)

failure_count = st.number_input(
    "Failure Event Count"
)

if st.button("Predict Failure Risk"):

    score = random.randint(1, 100)

    if score > 70:
        st.error(f"High Failure Risk ⚠️ ({score}%)")

    elif score > 40:
        st.warning(f"Medium Failure Risk ({score}%)")

    else:
        st.success(f"Low Failure Risk ✅ ({score}%)")
