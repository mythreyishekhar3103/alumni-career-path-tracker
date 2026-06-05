import streamlit as st
import pandas as pd
import joblib
import os

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Career Predictor",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🤖 Career Predictor")
st.markdown(
    """
    Predict the most suitable career path
    using Machine Learning.
    """
)

# --------------------------------------------------
# Load Models
# --------------------------------------------------

MODEL_PATH = "models/career_predictor.pkl"
SCALER_PATH = "models/scaler.pkl"
ENCODER_PATH = "models/label_encoder.pkl"

if (
    not os.path.exists(MODEL_PATH)
    or not os.path.exists(SCALER_PATH)
    or not os.path.exists(ENCODER_PATH)
):
    st.error(
        "Model files not found. Train the model first."
    )
    st.stop()

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
label_encoder = joblib.load(ENCODER_PATH)

# --------------------------------------------------
# User Inputs
# --------------------------------------------------

st.subheader("Enter Student Details")

col1, col2 = st.columns(2)

with col1:

    math_score = st.slider(
        "Mathematics Score",
        0,
        100,
        70
    )

    science_score = st.slider(
        "Science Score",
        0,
        100,
        70
    )

    communication = st.slider(
        "Communication Skill",
        0,
        100,
        70
    )

with col2:

    leadership = st.slider(
        "Leadership Skill",
        0,
        100,
        70
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

if st.button("Predict Career"):

    try:

        user_input = [[
            math_score,
            science_score,
            communication,
            leadership,
            creativity
        ]]

        user_input_scaled = scaler.transform(
            user_input
        )

        prediction = model.predict(
            user_input_scaled
        )

        predicted_career = (
            label_encoder.inverse_transform(
                prediction
            )[0]
        )

        st.success(
            f"🎯 Recommended Career: {predicted_career}"
        )

        # Probability if supported
        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(
                user_input_scaled
            )

            confidence = (
                probabilities.max() * 100
            )

            st.metric(
                "Confidence Score",
                f"{confidence:.2f}%"
            )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )

# --------------------------------------------------
# Information Section
# --------------------------------------------------

st.markdown("---")

st.info(
    """
    This prediction is based on the trained
    machine learning model using the
    Career Recommendation Dataset.

    Features Used:
    • Mathematics Score
    • Science Score
    • Communication
    • Leadership
    • Creativity
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Career Prediction Module"
)
