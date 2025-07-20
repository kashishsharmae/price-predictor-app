import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

df = pd.read_csv("housing.csv")
st.write("### 🧾 Sample Housing Data", df.head())

df['mainroad'] = df['mainroad'].map({'yes': 1, 'no': 0})
df['guestroom'] = df['guestroom'].map({'yes': 1, 'no': 0})
df['basement'] = df['basement'].map({'yes': 1, 'no': 0})
df['hotwaterheating'] = df['hotwaterheating'].map({'yes': 1, 'no': 0})
df['airconditioning'] = df['airconditioning'].map({'yes': 1, 'no': 0})

X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

def predict_price(area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwater, ac, parking):
    input_data = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwater, ac, parking]])
    prediction = model.predict(input_data)
    return prediction[0]

st.title("🏠 House Price Prediction App")
st.markdown("Enter the house details to get the predicted price:")

area = st.number_input("Area (sq ft)", min_value=500)
bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
stories = st.selectbox("Stories", [1, 2, 3, 4])
mainroad = st.radio("Main Road?", ['yes', 'no'])
guestroom = st.radio("Guest Room?", ['yes', 'no'])
basement = st.radio("Basement?", ['yes', 'no'])
hotwater = st.radio("Hot Water Heating?", ['yes', 'no'])
ac = st.radio("Air Conditioning?", ['yes', 'no'])
parking = st.slider("Parking Spaces", 0, 3)

mainroad = 1 if mainroad == 'yes' else 0
guestroom = 1 if guestroom == 'yes' else 0
basement = 1 if basement == 'yes' else 0
hotwater = 1 if hotwater == 'yes' else 0
ac = 1 if ac == 'yes' else 0

if st.button("Predict Price"):
    result = predict_price(area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwater, ac, parking)
    st.success(f"🏡 Estimated Price: ₹{round(result):,}")
