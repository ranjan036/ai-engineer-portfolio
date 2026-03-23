# ML Dataset Analyzer

This project analyzes datasets using Pandas.

## Features
- Load dataset
- Explore data
- Generate statistics
- Visualize features

#Day 2 (21 march , 2026):
Built data analyzer tool , initial version
My idea to built it as class 
Leanrn about
loading data , getting basic info, shape , columns
Statistical analysis 
Ploting histogram , to see how data is distributed 
converting a folder to python package , so that we can import module from src folder . or any other folder if we want

# Day 3 
# ML Dataset Analyzer

A reusable Python tool for:

- Data analysis
- Data preprocessing
- Model training
- Evaluation
- Prediction

## Features

- Supports any dataset
- Flexible model integration
- Clean modular design

## Usage

python main.py

PROJECT 1 — DEPLOYMENT DEBUG SUMMARY

🚀 Project: Iris Flower Predictor (ML + Streamlit)

---

❌ ISSUE 1: Missing Dependency (matplotlib)

Error:
ModuleNotFoundError: No module named 'matplotlib'

Cause:
matplotlib not included in requirements.txt

Fix:

- Added matplotlib to requirements.txt
- Pushed updated file to GitHub

---

❌ ISSUE 2: Multiple requirements.txt Conflict

Error:
Streamlit used wrong requirements file

Cause:
Two files existed:

- requirements.txt (root)
- requirements.txt (inside subfolder)

Fix:

- Deleted duplicate file from subfolder
- Kept only root requirements.txt

---

❌ ISSUE 3: Altair Version Conflict

Error:
No module named 'altair.vegalite.v4'

Cause:

- Streamlit version incompatible with latest Altair
- Version mismatch

Fix:

- Pinned versions:
  streamlit==1.19.0
  altair==4.2.2

---

❌ ISSUE 4: Python Compatibility (imghdr removed)

Error:
ModuleNotFoundError: No module named 'imghdr'

Cause:

- Python 3.14 used in cloud
- Older Streamlit depended on removed module

Fix:

- Upgraded Streamlit to newer version
- Ensured compatibility with Python 3.14

---

❌ ISSUE 5: Model Not Loading (Path Issue)

Error:
'NoneType' object has no attribute 'predict'

Cause:

- Incorrect relative path for model.pkl
- Working directory mismatch in cloud

Fix:

- Used absolute path with os:
  
  BASE_DIR = os.path.dirname(os.path.abspath(file))
  MODEL_PATH = os.path.join(BASE_DIR, "models/model.pkl")

---

❌ ISSUE 6: UnboundLocalError in predict()

Error:
cannot access local variable 'prediction'

Cause:

- prediction variable defined only inside condition
- Not initialized in all code paths

Fix:

- Simplified predict():
  
  prediction = self.model.predict([input_data])
  return prediction[0]

---

❌ ISSUE 7: Silent Exception Hiding Errors

Error:
App returning None without clear reason

Cause:

- try/except block hiding real error

Fix:

- Temporarily returned actual error message
- Identified root cause quickly

---

❌ ISSUE 8: Input Shape Handling

Issue:
Model expects 2D input

Cause:
Passing 1D list directly

Fix:

- Wrapped input:
  
  self.model.predict([input_data])

---

🧠 KEY LEARNINGS

✔ Deployment environment differs from local
✔ requirements.txt must be clean and unique
✔ Version compatibility is critical
✔ Never rely on relative paths in production
✔ Use file for robust path handling
✔ Avoid silent exception handling
✔ Always validate model loading
✔ ML models expect 2D input

---

🔥 FINAL OUTCOME

✔ Successfully deployed ML app on Streamlit Cloud
✔ Debugged multiple real-world issues
✔ Built end-to-end ML system (local → cloud)