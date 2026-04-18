import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
# Load the model
with open('../models/model.pkl', 'rb') as f:
    model = pkl.load(f)
# Define the Streamlit app

Model_Feature = pkl.load(open('../models/X_columns.pkl', 'rb'))


def main():
    st.title("Student Performance Prediction")
    st.write("Enter the following details to predict the student's performance:")
    # Input fields for the features
    gender = st.selectbox("Gender", ["male", "female"])
    race_ethnicity = st.selectbox("race", ["group A", "group B", "group C", "group D", "group E"])
    parental_level_of_education = st.selectbox("Parental Level of Education", ["high school", "some college", "associate's degree", "bachelor's degree", "master's degree","some high school"])
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"]) 
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    # Create a DataFrame for the input features
    input_dict = {col:0 for col in Model_Feature}

    #mapping UI to actual columns

    if gender == "male":
        input_dict["gender_male"] = 1

    if race_ethnicity != "group A":
        col_name = f"race/ethnicity_{race_ethnicity}"
        if col_name in input_dict:
            input_dict[col_name] = 1

    col_name = f"parental level of education_{parental_level_of_education}"    
    if col_name in input_dict:
        input_dict[col_name] = 1
    if lunch == "standard":
        input_dict["lunch_standard"] = 1

    if test_preparation_course == "none":
        input_dict["test preparation course_none"]= 1


    input_data = pd.DataFrame([input_dict])

    # Predict the performance
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.write(f"Predicted Performance: {prediction[0]:.2f}")

if __name__ == "__main__":
    main()        