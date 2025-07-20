# ✅ train_model.py — To train and create model.pkl

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset (you must have housing.csv in same folder)
data = pd.read_csv("housing.csv")

# Convert yes/no to 1/0 for binary features
binary_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning']
for col in binary_columns:
    data[col] = data[col].map({'yes': 1, 'no': 0})

# Features and label
X = data[['area', 'bedrooms', 'bathrooms', 'stories',
          'mainroad', 'guestroom', 'basement',
          'hotwaterheating', 'airconditioning', 'parking']]
y = data['price']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")



