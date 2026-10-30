import streamlit as st

print(st.__version__)



import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Telecom Customer Churn Prediction")

st.write("Enter customer details to predict churn.")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input(
    "Monthly Charges", min_value=0.0, value=70.0
)
total_charges = st.number_input(
    "Total Charges", min_value=0.0, value=840.0
)

if st.button("Predict Churn"):
    features = pd.DataFrame(
        [[tenure, monthly_charges, total_charges]],
        columns=["tenure", "MonthlyCharges", "TotalCharges"]
    )

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is likely to stay.")















