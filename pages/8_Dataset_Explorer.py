import streamlit as st
import pandas as pd

from src.utils import (
    load_data,
    search_dataframe,
    convert_to_csv
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📋",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📋 Dataset Explorer")
st.markdown(
    """
    Explore, search, filter and download
    datasets used in the Alumni Career Path Tracker.
    """
)

# --------------------------------------------------
# Dataset Selection
# --------------------------------------------------

datasets = {
    "Career Recommendation Dataset":
        "data/career_recommendation_dataset.csv",

    "Jobs Dataset":
        "data/jobss.csv",

    "Job Description Dataset":
        "data/job_title_des.csv",

    "Youth Unemployment Dataset":
        "data/youth_unemployment_global.csv",

    "Resume Dataset":
        "data/resume_dataset_200k_enhanced.csv"
}

selected_dataset = st.selectbox(
    "Select Dataset",
    list(datasets.keys())
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

try:

    df = load_data(
        datasets[selected_dataset]
    )

except Exception as e:

    st.error(
        f"Error Loading Dataset: {e}"
    )

    st.stop()

# --------------------------------------------------
# Dataset Summary
# --------------------------------------------------

st.subheader("📊 Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Rows",
        df.shape[0]
    )

with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )

with col3:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

with col4:
    st.metric(
        "Duplicates",
        int(df.duplicated().sum())
    )

# --------------------------------------------------
# Search Dataset
# --------------------------------------------------

st.subheader("🔍 Search Dataset")

search_text = st.text_input(
    "Enter keyword"
)

filtered_df = search_dataframe(
    df,
    search_text
)

# --------------------------------------------------
# Column Filter
# --------------------------------------------------

st.subheader("⚙️ Column Filter")

selected_columns = st.multiselect(
    "Select Columns",
    filtered_df.columns,
    default=list(filtered_df.columns)
)

filtered_df = filtered_df[
    selected_columns
]

# --------------------------------------------------
# Dataset Viewer
# --------------------------------------------------

st.subheader("📄 Dataset Preview")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=500
)

# --------------------------------------------------
# Data Types
# --------------------------------------------------

st.subheader("🧾 Column Information")

column_info = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(
    column_info,
    use_container_width=True
)

# --------------------------------------------------
# Missing Values Report
# --------------------------------------------------

st.subheader("⚠️ Missing Values")

missing_df = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum()
})

st.dataframe(
    missing_df,
    use_container_width=True
)

# --------------------------------------------------
# Download Dataset
# --------------------------------------------------

st.subheader("⬇️ Download Data")

csv_file = convert_to_csv(
    filtered_df
)

st.download_button(
    label="Download Filtered Dataset",
    data=csv_file,
    file_name="filtered_dataset.csv",
    mime="text/csv"
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Dataset Explorer"
)
