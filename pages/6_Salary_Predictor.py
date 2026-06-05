import streamlit as st
import pandas as pd
import joblib
import os

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("💰 Salary Predictor")
st.markdown(
    """
    Predict expected salary based on
    experience and skill ratings.
    """
)

# --------------------------------------------------
# Model Paths
# --------------------------------------------------

MODEL_PATH = "models/salary_predictor.pkl"
SCALER_PATH = "models/scaler.pkl"

# --------------------------------------------------
# Check Model Availability
# --------------------------------------------------

if not os.path.exists(MODEL_PATH):

    st.warning(
        """
        salary_predictor.pkl not found.

        Train the salary prediction model first
        or add the model file to the models folder.
        """
    )

    st.stop()

# --------------------------------------------------
# Load Model
# --------------------------------------------------

salary_model = joblib.load(MODEL_PATH)

if os.path.exists(SCALER_PATH):
    scaler = joblib.load(SCALER_PATH)
else:
    scaler = None

# --------------------------------------------------
# User Inputs
# --------------------------------------------------

st.subheader("Enter Candidate Details")

col1, col2 = st.columns(2)

with col1:

    experience = st.slider(
        "Years of Experience",
        0,
        20,
        2
    )

    communication = st.slider(
        "Communication Skill",
        0,
        100,
        70
    )

    leadership = st.slider(
        "Leadership Skill",
        0,
        100,
        70
    )

with col2:

    technical_skill = st.slider(
        "Technical Skill",
        0,
        100,
        75
    )

    creativity = st.slider(
        "Creativity",
        0,
        100,
        70
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Salary"):

    try:

        input_data = [[
            experience,
            communication,
            leadership,
            technical_skill,
            creativity
        ]]

        if scaler:
            input_data = scaler.transform(
                input_data
            )

        predicted_salary = (
            salary_model.predict(
                input_data
            )[0]
        )

        st.success(
            f"💵 Predicted Salary: ₹ {predicted_salary:,.0f}"
        )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )

# --------------------------------------------------
# Salary Insights
# --------------------------------------------------

st.markdown("---")

st.subheader("📊 Salary Prediction Factors")

st.info(
    """
    Salary estimation is influenced by:

    • Experience

    • Communication Skills

    • Leadership Ability

    • Technical Skills

    • Creativity

    The prediction accuracy depends on
    the quality of training data.
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Salary Prediction Module"
)
