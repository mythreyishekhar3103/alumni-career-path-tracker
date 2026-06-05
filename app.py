import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Alumni Career Path Tracker",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Hide Streamlit Branding
# --------------------------------------------------

hide_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

st.markdown(
    hide_style,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🎓 Alumni Career Path Tracker")

st.sidebar.info(
    """
    Navigate using the pages menu.

    📊 Dashboard

    📈 Career Analytics

    🔄 Career Flow

    🗺️ Geo Analytics

    🤖 Career Predictor

    💰 Salary Predictor

    🎯 Skill Gap Analyzer

    📋 Dataset Explorer

    ℹ️ About
    """
)

# --------------------------------------------------
# Main Header
# --------------------------------------------------

st.title("🎓 Alumni Career Path Tracker")

st.markdown("""
### Data Analytics & Machine Learning Platform

Analyze alumni career journeys, hiring trends, skills demand,
salary insights, and career growth opportunities using
interactive dashboards and machine learning.

---
""")

# --------------------------------------------------
# Feature Cards
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        """
        📊 Dashboard

        View KPIs, job statistics,
        salary insights, and trends.
        """
    )

with col2:

    st.info(
        """
        📈 Career Analytics

        Explore hiring patterns,
        skills demand, and recruiters.
        """
    )

with col3:

    st.info(
        """
        🔄 Career Flow

        Interactive Sankey diagrams
        showing career transitions.
        """
    )

col4, col5, col6 = st.columns(3)

with col4:

    st.success(
        """
        🗺️ Geo Analytics

        Discover hiring hotspots
        and location-based trends.
        """
    )

with col5:

    st.success(
        """
        🤖 Career Predictor

        Predict suitable career
        paths using ML models.
        """
    )

with col6:

    st.success(
        """
        💰 Salary Predictor

        Estimate salaries based
        on skills and experience.
        """
    )

# --------------------------------------------------
# Additional Features
# --------------------------------------------------

st.subheader("🚀 Advanced Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:

    st.markdown("""
    ### 🎯 Skill Gap Analysis

    Compare your skills with
    market-demand skills and
    identify missing competencies.
    """)

with feature2:

    st.markdown("""
    ### 📋 Dataset Explorer

    Explore, search, filter,
    and download datasets.
    """)

with feature3:

    st.markdown("""
    ### 📈 Career Intelligence

    Gain insights into career
    growth and industry trends.
    """)

# --------------------------------------------------
# Technology Stack
# --------------------------------------------------

st.subheader("🛠️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("Frontend", "Streamlit")
tech2.metric("Analytics", "Pandas")
tech3.metric("Visualization", "Plotly")
tech4.metric("ML", "Scikit-Learn")

# --------------------------------------------------
# Datasets Used
# --------------------------------------------------

st.subheader("📂 Datasets Used")

st.markdown("""
- career_recommendation_dataset.csv
- jobss.csv
- job_title_des.csv
- youth_unemployment_global.csv
- resume_dataset_200k_enhanced.csv
""")

# --------------------------------------------------
# Project Outcome
# --------------------------------------------------

st.subheader("🏆 Project Outcome")

st.success("""
This platform helps students, alumni, and professionals:

✔ Understand career trends

✔ Identify in-demand skills

✔ Discover hiring companies

✔ Predict career opportunities

✔ Analyze salary expectations

✔ Explore job market insights

✔ Visualize career progression pathways
""")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Data Analytics & Machine Learning Project"
)
