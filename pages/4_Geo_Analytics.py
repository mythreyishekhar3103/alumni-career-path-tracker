import streamlit as st
import plotly.express as px

from src.utils import load_data

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Geo Analytics",
    page_icon="🗺️",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🗺️ Geo Analytics")
st.markdown(
    """
    Analyze job opportunities, hiring hotspots,
    and geographic career trends.
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

with st.expander("📄 Dataset Preview"):

    st.dataframe(
        jobs_df.head(10),
        use_container_width=True
    )

# --------------------------------------------------
# Check Required Columns
# --------------------------------------------------

required_columns = [
    "Latitude",
    "Longitude"
]

missing_columns = [
    col
    for col in required_columns
    if col not in jobs_df.columns
]

if missing_columns:

    st.warning(
        f"Missing Columns: {missing_columns}"
    )

    st.stop()

# --------------------------------------------------
# Job Location Map
# --------------------------------------------------

st.subheader("📍 Job Market Map")

hover_column = None

possible_hover = [
    "Location",
    "Role",
    "Job Title",
    "Company"
]

for col in possible_hover:

    if col in jobs_df.columns:
        hover_column = col
        break

fig = px.scatter_mapbox(
    jobs_df,
    lat="Latitude",
    lon="Longitude",
    hover_name=hover_column,
    zoom=3,
    height=600
)

fig.update_layout(
    mapbox_style="open-street-map",
    margin=dict(
        l=0,
        r=0,
        t=40,
        b=0
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# Location Analysis
# --------------------------------------------------

st.subheader("🏙️ Top Hiring Locations")

if "Location" in jobs_df.columns:

    location_df = (
        jobs_df["Location"]
        .value_counts()
        .head(15)
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

# --------------------------------------------------
# Salary by Location
# --------------------------------------------------

st.subheader("💰 Salary by Location")

if (
    "Location" in jobs_df.columns and
    "sal" in jobs_df.columns
):

    salary_df = (
        jobs_df.groupby("Location")["sal"]
        .mean()
        .sort_values(
            ascending=False
        )
        .head(15)
        .reset_index()
    )

    fig = px.bar(
        salary_df,
        x="Location",
        y="sal",
        title="Average Salary by Location"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# Geo Insights
# --------------------------------------------------

st.subheader("📌 Geographic Insights")

total_locations = (
    jobs_df["Location"].nunique()
    if "Location" in jobs_df.columns
    else 0
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Unique Locations",
        total_locations
    )

with col2:

    st.metric(
        "Total Jobs",
        len(jobs_df)
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Alumni Career Path Tracker | Geo Analytics"
)
