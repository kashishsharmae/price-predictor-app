# 🏠 Price Predictor App (Streamlit)

A machine learning web app to predict house prices using key property features. Built with **Python**, **Streamlit**, and **Scikit-learn**.

---

## 📌 Features
- Predicts house prices based on:
  - Area (sq ft)
  - Bedrooms, Bathrooms, Stories
  - Road access, Guestroom, Basement
  - Hot water heating, Air Conditioning, Parking
- ✅ Added **Region** and **Top 25 Expensive Cities** selection
- Simple, responsive user interface built using **Streamlit**

---

## 📁 Folder Structure

```
📦 price-predictor-app/
├── app.py                # Streamlit app UI
├── train_model.py        # Model training script
├── model.pkl             # Trained ML model
├── requirements.txt      # Required libraries
├── README.md             # Project documentation
└── housing.csv           # Dataset (you must provide this file)
```

---

## 🚀 How to Run the App Locally (VS Code or Terminal)

### 1. Clone the repo or download ZIP
```bash
git clone https://github.com/your-username/price-predictor-app.git
cd price-predictor-app
```

### 2. (Optional) Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model (if not done)
```bash
python train_model.py
```

### 5. Run the Streamlit App
```bash
streamlit run app.py
```

Go to: [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Deployed App
Visit the hosted version:  
👉 [https://prices-predictor-app.streamlit.app](https://prices-predictor-app.streamlit.app)

---

## 🧠 Tech Stack
- Python 3.10+
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## ✍️ Author
**Kashish Sharma**  
🔗 GitHub: [@kashishsharmae](https://github.com/kashishsharmae)

---

## 📄 License
This project is open-source and free to use for educational purposes.
