import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("linear_model.pkl")

# App Title
st.title("Stock Price Prediction App")
st.write("Enter stock features to predict the closing price using the trained Linear Regression model.")

# Input fields
open_val = st.number_input("Open", value=100.0)
high_val = st.number_input("High", value=220.0)
low_val = st.number_input("Low", value=200.0)
volume_val = st.number_input("Volume", value=30000)

# Predict button
if st.button("Predict Closing Price"):
    input_data = np.array([[open_val, high_val, low_val, volume_val]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Close Price: ₹{float(prediction[0]):.2f}")
