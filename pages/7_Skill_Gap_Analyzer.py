import streamlit as st
import pandas as pd

from src.utils import load_data

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🎯 Skill Gap Analyzer")
st.markdown(
    """
    Compare your current skills with market-demand skills
    and identify missing skills for career growth.
    """
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

try:
    jobs_df = load_data("data/jobss.csv")

except Exception as e:
    st.error(f"Dataset Loading Error: {e}")
    st.stop()

# --------------------------------------------------
# Detect Skills Column
# --------------------------------------------------

skill_column = None

possible_skill_columns = [
    "Skills",
    "skills",
    "Skill",
    "skill"
]

for col in possible_skill_columns:
    if col in jobs_df.columns:
        skill_column = col
        break

if skill_column is None:

    st.warning(
        "No skills column found in jobss.csv"
    )

    st.stop()

# --------------------------------------------------
# Extract Market Skills
# --------------------------------------------------

market_skills = []

for row in jobs_df[skill_column].dropna():

    skills = str(row).split(",")

    for skill in skills:
        market_skills.append(
            skill.strip().lower()
        )

market_skills = sorted(
    list(set(market_skills))
)

# --------------------------------------------------
# User Input
# --------------------------------------------------

st.subheader("Enter Your Skills")

user_skills = st.multiselect(
    "Select Skills",
    market_skills
)

# --------------------------------------------------
# Analysis
# --------------------------------------------------

if st.button("Analyze Skill Gap"):

    if len(user_skills) == 0:

        st.warning(
            "Please select at least one skill."
        )

    else:

        missing_skills = list(
            set(market_skills) -
            set(user_skills)
        )

        st.success(
            f"Skills You Have: {len(user_skills)}"
        )

        st.metric(
            "Total Market Skills",
            len(market_skills)
        )

        st.metric(
            "Missing Skills",
            len(missing_skills)
        )

        # -----------------------------
        # Top Recommended Skills
        # -----------------------------

        st.subheader(
            "🚀 Recommended Skills"
        )

        recommended = missing_skills[:20]

        st.write(
            ", ".join(recommended)
        )

        # -----------------------------
        # Skill Coverage
        # -----------------------------

        coverage = (
            len(user_skills)
            /
            len(market_skills)
        ) * 100

        st.progress(
            int(coverage)
        )

        st.info(
            f"Skill Coverage: {coverage:.2f}%"
        )

# --------------------------------------------------
# Market Skills Overview
# --------------------------------------------------

st.markdown("---")

st.subheader(
    "📊 Top Market Skills"
)

skill_count = {}

for row in jobs_df[skill_column].dropna():

    for skill in str(row).split(","):

        skill = skill.strip()

        skill_count[skill] = (
            skill_count.get(skill, 0) + 1
        )

top_skills = (
    pd.DataFrame(
        skill_count.items(),
        columns=["Skill", "Count"]
    )
    .sort_values(
        by="Count",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    top_skills,
    use_container_width=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Skill Gap Analyzer"
)
