#import lib
import streamlit as st
from src.dataset_analyzer import DataSetAnalyzer

#load model
analyzer = DataSetAnalyzer(None)

DEFAULT_MODEL_PATH = "../../models/model.pkl"

analyzer.load_model(DEFAULT_MODEL_PATH)

#UI
#Title
st.title("🌸 Iris Flower Predictor")
st.write("Enter 🌸 measurements.")
#input fields
col1, col2 = st.columns(2)
with col1:
    sepal_length = st.number_input("Sepal Length",value= 5.1)
    sepal_width = st.number_input("Sepal Width", value= 3.5)

with col2:
    petal_length = st.number_input("Petal Length",value=1.4)
    petal_width = st.number_input("Petal Width",value=0.2)

#predict button
if st.button("Predict"):
    with st.spinner("predicting..."):
        input_data = [sepal_length, sepal_width, petal_length, petal_width]
        result = analyzer.predict(input_data)
        st.success(f"🌸 Predicted Flower:{result}")


