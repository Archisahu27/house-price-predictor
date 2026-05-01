# app.py

import streamlit as st
from predict import predict_price

st.title("🏠 House Price Predictor")

st.write("Enter details to predict house price")

# Inputs
rm = st.number_input("Average number of rooms (rm)", min_value=0.0, step=0.1)
lstat = st.number_input("Lower status population (%) (lstat)", min_value=0.0, step=0.1)
ptratio = st.number_input("Pupil-teacher ratio (ptratio)", min_value=0.0, step=0.1)

# Button
if st.button("Predict Price"):
    price = predict_price(rm, lstat, ptratio)
    st.success(f"Predicted House Price: ${price}")