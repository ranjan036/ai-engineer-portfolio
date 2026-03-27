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
📘 NYC Taxi EDA – Learning Notes (Day 1)

🧠 Core Concepts Learned

1️⃣ Boolean Filtering (Most Important)
- Created conditions using:
  column == value
  column < value
  column > value
- Result → Boolean Series (True / False)
- Used .sum() to count True values

👉 Learned:
(condition).sum() → counts matching rows


2️⃣ Vectorized Operations (No Loops 🚀)
- Avoided for loops
- Used pandas operations on entire column

👉 Example:
df['col'] == 0 → applied to entire column


3️⃣ Data Type Inspection
Methods explored:
- df.info() → structure overview
- df.dtypes → column datatypes
- select_dtypes() → filter columns by type

👉 Learned:
Datatype ≠ Actual meaning


4️⃣ Datetime Handling
Method:
- pd.to_datetime()

👉 Used for:
Convert string → datetime


5️⃣ Timedelta Concept (Advanced ⭐)
- datetime - datetime → timedelta

Method:
- pd.Timedelta()

👉 Used for:
Compare durations (not integers)


6️⃣ Logical Data Validation (Real EDA 🔥)

✔ Trip Duration
- Found extreme values (~40 days → invalid)

✔ Passenger Count
- Found invalid values (0 passengers → 60 rows)

✔ Datetime Consistency
- Verified dropoff > pickup (no issues found)

✔ Coordinates Validation
- Latitude range: 40–41
- Longitude range: -75 to -73
- Found ~277 invalid latitude rows
- Found ~41 invalid longitude rows

👉 Learned:
Data can be present but still invalid


7️⃣ Domain Knowledge Integration 🌍
- Applied real-world NYC geography
- Used it to detect anomalies


8️⃣ Efficient Thinking Pattern
Condition → Boolean → Aggregation

Used for:
- counting anomalies
- validating data


9️⃣ Clean Code Thinking
- Convert once → reuse later
- Avoid repeated computation
- Think pipeline: RAW → CLEAN → READY


🔥 Key Takeaways

✔ Missing values = 0 does NOT mean clean data
✔ Real EDA = logical validation, not just plotting
✔ Avoid loops → use vectorization
✔ Data type understanding is critical
✔ Always apply real-world constraints

## 👨‍💻 Author
Ranjan Ali