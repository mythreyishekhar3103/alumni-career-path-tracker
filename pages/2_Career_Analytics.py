import streamlit as st
import pandas as pd
import plotly.express as px

from src.utils import load_data

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Career Analytics",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📈 Career Analytics")
st.markdown(
    "Analyze career trends, skills, recruiters, and job market insights."
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
# Dataset Preview
# --------------------------------------------------

with st.expander("View Dataset"):

    st.dataframe(
        jobs_df.head(20),
        use_container_width=True
    )

# --------------------------------------------------
# Top Job Roles
# --------------------------------------------------

st.subheader("💼 Top Job Roles")

role_col = None

possible_roles = [
    "Role",
    "Job Title",
    "jobtitle",
    "Role Category"
]

for col in possible_roles:
    if col in jobs_df.columns:
        role_col = col
        break

if role_col:

    role_df = (
        jobs_df[role_col]
        .value_counts()
        .head(10)
        .reset_index()
    )

    role_df.columns = [
        "Role",
        "Count"
    ]

    fig = px.bar(
        role_df,
        x="Role",
        y="Count",
        title="Top Job Roles"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.warning("Role column not found.")

# --------------------------------------------------
# Experience Analysis
# --------------------------------------------------

st.subheader("📊 Experience Distribution")

exp_col = None

possible_exp = [
    "Experience",
    "experience"
]

for col in possible_exp:
    if col in jobs_df.columns:
        exp_col = col
        break

if exp_col:

    fig = px.histogram(
        jobs_df,
        x=exp_col,
        title="Experience Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.warning("Experience column not found.")

# --------------------------------------------------
# Top Hiring Locations
# --------------------------------------------------

st.subheader("📍 Top Hiring Locations")

if "Location" in jobs_df.columns:

    location_df = (
        jobs_df["Location"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    location_df.columns = [
        "Location",
        "Jobs"
    ]

    fig = px.bar(
        location_df,
        x="Location",
        y="Jobs",
        title="Top Hiring Locations"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.warning("Location column not found.")

# --------------------------------------------------
# Salary Analysis
# --------------------------------------------------

st.subheader("💰 Salary Analysis")

if "sal" in jobs_df.columns:

    fig = px.box(
        jobs_df,
        y="sal",
        title="Salary Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.warning("Salary column not found.")

# --------------------------------------------------
# Skills Analysis
# --------------------------------------------------

st.subheader("🎯 Skills Analysis")

skill_col = None

possible_skills = [
    "Skills",
    "skills"
]

for col in possible_skills:
    if col in jobs_df.columns:
        skill_col = col
        break

if skill_col:

    skills = []

    for row in jobs_df[skill_col].dropna():

        for skill in str(row).split(","):
            skills.append(skill.strip())

    skill_df = (
        pd.Series(skills)
        .value_counts()
        .head(15)
        .reset_index()
    )

    skill_df.columns = [
        "Skill",
        "Count"
    ]

    fig = px.bar(
        skill_df,
        x="Skill",
        y="Count",
        title="Most Demanded Skills"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.warning("Skills column not found.")

# --------------------------------------------------
# Insights
# --------------------------------------------------

st.subheader("📌 Key Insights")

st.info(
    """
    • Identify top hiring roles.
    
    • Discover high-demand skills.
    
    • Analyze salary distribution.
    
    • Explore location-wise opportunities.
    
    • Understand experience requirements.
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")
st.caption(
    "Alumni Career Path Tracker | Career Analytics Module"
)
