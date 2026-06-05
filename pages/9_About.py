import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("ℹ️ About Alumni Career Path Tracker")

# --------------------------------------------------
# Project Overview
# --------------------------------------------------

st.header("📌 Project Overview")

st.markdown("""
The **Alumni Career Path Tracker** is a Data Analytics and Machine Learning platform
designed to analyze career journeys, job market trends, skills demand,
salary patterns, and career growth opportunities.

The platform combines multiple datasets and advanced analytics to help students,
graduates, and professionals understand:

- Career opportunities
- Industry hiring trends
- Skill requirements
- Salary expectations
- Career progression pathways
- Geographic job distribution
""")

# --------------------------------------------------
# Objectives
# --------------------------------------------------

st.header("🎯 Project Objectives")

st.markdown("""
- Analyze career progression trends
- Identify top hiring industries
- Discover in-demand skills
- Predict suitable career paths
- Estimate salary expectations
- Perform skill gap analysis
- Visualize career transitions using Sankey Diagrams
- Explore job opportunities geographically
""")

# --------------------------------------------------
# Datasets Used
# --------------------------------------------------

st.header("📂 Datasets Used")

datasets = [
    "career_recommendation_dataset.csv",
    "jobss.csv",
    "job_title_des.csv",
    "youth_unemployment_global.csv",
    "resume_dataset_200k_enhanced.csv"
]

for dataset in datasets:
    st.markdown(f"✅ {dataset}")

# --------------------------------------------------
# Technologies
# --------------------------------------------------

st.header("🛠️ Technologies Used")

tech_stack = [
    "Python",
    "Pandas",
    "NumPy",
    "Plotly",
    "Streamlit",
    "Scikit-Learn",
    "Joblib",
    "Machine Learning",
    "Data Analytics"
]

for tech in tech_stack:
    st.markdown(f"🔹 {tech}")

# --------------------------------------------------
# Machine Learning Models
# --------------------------------------------------

st.header("🤖 Machine Learning Models")

models = [
    "Career Prediction Model",
    "Salary Prediction Model",
    "Skill Gap Analysis Engine",
    "Recruiter Recommendation System"
]

for model in models:
    st.markdown(f"✅ {model}")

# --------------------------------------------------
# Features
# --------------------------------------------------

st.header("🚀 Key Features")

features = [
    "Interactive Dashboard",
    "Career Analytics",
    "Career Flow Sankey Diagram",
    "Geo Analytics",
    "Career Prediction",
    "Salary Prediction",
    "Skill Gap Analyzer",
    "Dataset Explorer"
]

for feature in features:
    st.markdown(f"📌 {feature}")

# --------------------------------------------------
# Repository Structure
# --------------------------------------------------

st.header("📁 Repository Structure")

st.code("""
alumni-career-path-tracker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
├── models/
├── notebooks/
├── pages/
├── src/
└── assets/
""")

# --------------------------------------------------
# Future Enhancements
# --------------------------------------------------

st.header("🔮 Future Enhancements")

st.markdown("""
- AI Career Chatbot
- Resume Analyzer
- Job Recommendation System
- Real-time Job Market Analysis
- Alumni Networking Dashboard
- Industry Demand Forecasting
- Deep Learning Models
""")

# --------------------------------------------------
# Project Outcome
# --------------------------------------------------

st.header("🏆 Expected Outcome")

st.success("""
The platform helps students and professionals understand
career trends, required skills, salary expectations,
industry demands, and career growth opportunities
through advanced analytics and machine learning.
""")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Data Analytics & Machine Learning Project"
)
