# 🚖 NYC Taxi Trip Duration Prediction

## 📌 Project Overview
This project focuses on analyzing and predicting NYC taxi trip durations using real-world data.

The goal is to build an end-to-end machine learning pipeline:
- Data Exploration (EDA)
- Data Cleaning
- Feature Engineering
- Model Training & Evaluation
- (Future) Deployment as a web app

Project Structure :
ml/
 └── nyc-taxi/
      ├── data/
      │     ├── raw/
      │     └── processed/
      │
      ├── notebooks/
      │     └── eda.ipynb
      │
      ├── src/
      │     ├── cleaning.py
      │     ├── feature_engineering.py
      │     ├── train.py
      │     └── predict.py
      │
      ├── models/
      │     └── model.pkl
      │
      ├── app/
      │     └── app.py   (later)
      │
      ├── requirements.txt
      └── README.md

## 📊 Dataset
- NYC Taxi Trip Duration dataset (Kaggle)
- Contains real-world taxi trip data including:
  - Pickup & dropoff timestamps
  - Passenger count
  - Location coordinates
  - Trip duration (target)

---

## 🔍 Exploratory Data Analysis (EDA)
Key steps:
- Understanding data structure
- Handling missing values
- Detecting outliers
- Analyzing distributions
- Identifying anomalies

---

## 🧹 Data Cleaning
- Removing invalid records
- Handling missing values
- Filtering unrealistic trip durations
- Fixing data inconsistencies

---

## ⚙️ Feature Engineering
- Extracting time-based features (hour, day, etc.)
- Distance calculation (Haversine)
- Encoding categorical variables

---

## 🤖 Model
- Algorithms: (To be added)
- Evaluation Metrics: (To be added)

---

## 🚀 Future Improvements
- Build Streamlit app for predictions
- Compare multiple models
- Hyperparameter tuning
- Deploy on cloud

---

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- Streamlit (planned)

---

## 📈 Learnings
- Working with large datasets
- Real-world data cleaning challenges
- Feature engineering techniques
- End-to-end ML pipeline building

---

## 👨‍💻 Author
Ranjan Ali