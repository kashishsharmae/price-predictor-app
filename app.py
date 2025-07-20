
# 📁 Enhanced Price Predictor App with Region and 25 Expensive Cities

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Define Regions and Cities
regions = {
    'North': ['Delhi', 'Gurgaon', 'Noida', 'Chandigarh', 'Lucknow'],
    'South': ['Bangalore', 'Hyderabad', 'Chennai', 'Cochin', 'Vizag'],
    'East': ['Kolkata', 'Bhubaneswar', 'Patna', 'Ranchi', 'Guwahati'],
    'West': ['Mumbai', 'Pune', 'Ahmedabad', 'Jaipur', 'Surat'],
    'Central': ['Bhopal', 'Nagpur', 'Indore', 'Raipur', 'Jabalpur'],
    'Other': ['Shimla', 'Dehradun', 'Goa', 'Varanasi', 'Agra']
}

# App title
st.set_page_config(page_title="🏠 House Price Predictor", layout="centered")
st.title("🏠 House Price Predictor")

# Location selection
st.subheader("📍 Select Location")
selected_region = st.selectbox("Select Region", list(regions.keys()))
selected_city = st.selectbox("Select City", regions[selected_region])

# Property features
st.subheader("🏗 Property Details")
area = st.number_input("Area (in sq ft)", min_value=1, max_value=10000, value=1000)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
stories = st.selectbox("Number of Stories", [1, 2, 3, 4])
mainroad = st.radio("Located on Main Road?", ["yes", "no"])
guestroom = st.radio("Guestroom Available?", ["yes", "no"])
basement = st.radio("Basement Present?", ["yes", "no"])
hotwaterheating = st.radio("Hot Water Heating?", ["yes", "no"])
airconditioning = st.radio("Air Conditioning?", ["yes", "no"])
parking = st.selectbox("Parking Spaces", [0, 1, 2, 3])

# Convert categorical to numeric
def to_binary(value):
    return 1 if value == "yes" else 0

input_df = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'mainroad': [to_binary(mainroad)],
    'guestroom': [to_binary(guestroom)],
    'basement': [to_binary(basement)],
    'hotwaterheating': [to_binary(hotwaterheating)],
    'airconditioning': [to_binary(airconditioning)],
    'parking': [parking]
})

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: ₹{int(prediction):,}")
    st.info(f"📍 Location: {selected_city}, {selected_region} region")

# Footer
st.markdown("""
---
Made with ❤️ by Kashish Sharma  
[GitHub](https://github.com/kashishsharmae)
""")
