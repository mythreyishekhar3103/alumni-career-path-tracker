import streamlit as st
import pandas as pd

from src.utils import load_data
from src.sankey import (
    create_sankey_from_dataframe
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Career Flow",
    page_icon="🔄",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🔄 Career Flow Analysis")
st.markdown(
    """
    Explore career transitions and skill-to-role pathways
    using interactive Sankey diagrams.
    """
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

with st.expander("📄 View Dataset Preview"):

    st.dataframe(
        jobs_df.head(10),
        use_container_width=True
    )

# --------------------------------------------------
# Column Selection
# --------------------------------------------------

st.subheader("⚙️ Select Career Flow")

available_columns = jobs_df.columns.tolist()

source_column = st.selectbox(
    "Source Column",
    available_columns
)

target_column = st.selectbox(
    "Target Column",
    available_columns,
    index=min(1, len(available_columns)-1)
)

# --------------------------------------------------
# Generate Sankey Diagram
# --------------------------------------------------

if st.button("Generate Career Flow"):

    try:

        temp_df = jobs_df[
            [source_column, target_column]
        ].dropna()

        fig = create_sankey_from_dataframe(
            temp_df,
            source_column,
            target_column,
            title=f"{source_column} → {target_column}"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Unable to generate Sankey Diagram.\n{e}"
        )

# --------------------------------------------------
# Predefined Career Flows
# --------------------------------------------------

st.subheader("🚀 Quick Career Flows")

col1, col2 = st.columns(2)

with col1:

    if (
        "Skills" in jobs_df.columns and
        "Role" in jobs_df.columns
    ):

        if st.button("Skills → Role"):

            fig = create_sankey_from_dataframe(
                jobs_df,
                "Skills",
                "Role",
                "Skills → Role Flow"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

with col2:

    if (
        "Role Category" in jobs_df.columns and
        "Role" in jobs_df.columns
    ):

        if st.button("Role Category → Role"):

            fig = create_sankey_from_dataframe(
                jobs_df,
                "Role Category",
                "Role",
                "Role Category → Role Flow"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# --------------------------------------------------
# Insights Section
# --------------------------------------------------

st.subheader("📌 Career Flow Insights")

st.info(
    """
    Sankey diagrams help identify:

    • Popular career transitions

    • High-demand skill pathways

    • Industry role distributions

    • Skill-to-job relationships

    • Emerging career trends
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Career Flow Analytics"
)
