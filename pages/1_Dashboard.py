import streamlit as st
import pandas as pd

from src.utils import load_data
from src.analytics import (
    dataset_summary,
    get_average_salary,
    get_total_jobs
)

from src.visualizations import (
    salary_distribution,
    location_chart
)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📊 Alumni Career Path Tracker")
st.markdown(
    "### AI-Powered Career Analytics Dashboard"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

try:
    jobs_df = load_data("data/jobss.csv")

except Exception as e:
    st.error(f"Error Loading Dataset: {e}")
    st.stop()

# --------------------------------------------------
# KPI Section
# --------------------------------------------------

summary = dataset_summary(jobs_df)

total_jobs = get_total_jobs(jobs_df)

avg_salary = get_average_salary(
    jobs_df,
    salary_column="sal"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Jobs",
        f"{total_jobs:,}"
    )

with col2:
    st.metric(
        "Average Salary",
        f"₹ {avg_salary:,.0f}"
    )

with col3:
    st.metric(
        "Columns",
        summary["Columns"]
    )

with col4:
    st.metric(
        "Missing Values",
        summary["Missing Values"]
    )

st.divider()

# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------

st.subheader("📄 Dataset Preview")

st.dataframe(
    jobs_df.head(10),
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Salary Distribution
# --------------------------------------------------

st.subheader("💰 Salary Distribution")

if "sal" in jobs_df.columns:

    fig = salary_distribution(
        jobs_df,
        salary_column="sal"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.warning(
        "Salary column 'sal' not found."
    )

st.divider()

# --------------------------------------------------
# Top Hiring Locations
# --------------------------------------------------

st.subheader("📍 Top Hiring Locations")

if "Location" in jobs_df.columns:

    fig = location_chart(
        jobs_df,
        location_column="Location"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.warning(
        "Location column not found."
    )

st.divider()

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

st.subheader("📑 Dataset Information")

st.write(
    f"Rows: {jobs_df.shape[0]}"
)

st.write(
    f"Columns: {jobs_df.shape[1]}"
)

st.write(
    f"Duplicate Rows: {jobs_df.duplicated().sum()}"
)

st.write(
    f"Missing Values: {jobs_df.isnull().sum().sum()}"
)

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    ---
    Alumni Career Path Tracker
    Built with Streamlit, Pandas, Plotly & Machine Learning
    """
)
