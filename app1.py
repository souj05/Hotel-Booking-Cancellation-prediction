import streamlit as st
import joblib
import pandas as pd

model = joblib.load("hotel_cancellation_model.pkl")

st.title("Hotel Booking Cancellation Prediction")

st.set_page_config(page_title="Hotel Booking Cancellation Prediction",layout="wide")

st.title("🏨 Hotel Booking Cancellation Prediction")

st.sidebar.header("Customer Information")

lead_time = st.number_input("Lead Time", min_value=0)
adr = st.number_input("ADR", min_value=0.0)
adults = st.number_input("Adults", min_value=1)
children = st.number_input("Children", min_value=0)
babies = st.number_input("Babies", min_value=0)

arrival_week = st.slider("Arrival Week Number", 1, 53)
arrival_year = st.selectbox("Arrival Year",[2015,2016,2017])

country = st.number_input("Country Encoded", min_value=0)

previous_cancellations = st.number_input(
    "Previous Cancellations",
    min_value=0
)

booking_changes = st.number_input(
    "Booking Changes",
    min_value=0
)

special_requests = st.number_input(
    "Total Special Requests",
    min_value=0
)

if st.button("Predict Cancellation"):
    st.success("Prediction will be shown here")