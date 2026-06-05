import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------------------
# Page Config
# -----------------------------------------

st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Salary Predictor")

# -----------------------------------------
# Load Dataset
# -----------------------------------------

df = pd.read_csv(
    "data/jobss.csv"
)

# -----------------------------------------
# Load Models
# -----------------------------------------

try:

    model = joblib.load(
        "models/salary_predictor.pkl"
    )

    role_encoder = joblib.load(
        "models/role_encoder.pkl"
    )

    industry_encoder = joblib.load(
        "models/industry_encoder.pkl"
    )

    location_encoder = joblib.load(
        "models/location_encoder.pkl"
    )

except:

    st.error(
        """
        salary_predictor.pkl not found.

        Run:

        python src/train_salary_model.py
        """
    )

    st.stop()

# -----------------------------------------
# User Inputs
# -----------------------------------------

st.subheader("Enter Details")

experience = st.slider(
    "Experience (Years)",
    0,
    20,
    2
)

role_category = st.selectbox(
    "Role Category",
    sorted(
        df["Role Category"]
        .dropna()
        .unique()
    )
)

industry = st.selectbox(
    "Industry",
    sorted(
        df["Industry"]
        .dropna()
        .unique()
    )
)

location = st.selectbox(
    "Location",
    sorted(
        df["Location"]
        .dropna()
        .unique()
    )
)

# -----------------------------------------
# Prediction
# -----------------------------------------

if st.button(
    "Predict Salary"
):

    try:

        role_value = role_encoder.transform(
            [role_category]
        )[0]

        industry_value = industry_encoder.transform(
            [industry]
        )[0]

        location_value = location_encoder.transform(
            [location]
        )[0]

        input_data = pd.DataFrame(
            [[
                experience,
                role_value,
                industry_value,
                location_value
            ]],
            columns=[
                "Experience",
                "Role Category",
                "Industry",
                "Location"
            ]
        )

        salary = model.predict(
            input_data
        )[0]

        st.success(
            f"Estimated Salary: ₹ {salary:,.0f}"
        )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )

# -----------------------------------------
# Footer
# -----------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Salary Predictor"
)
