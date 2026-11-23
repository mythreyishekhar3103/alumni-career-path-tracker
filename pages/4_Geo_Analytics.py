
import streamlit as st
import plotly.express as px
import pandas as pd

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

# Create a separate dataframe for map
map_df = jobs_df.copy()

# Convert latitude and longitude into numeric values
map_df["Latitude"] = pd.to_numeric(
    map_df["Latitude"],
    errors="coerce"
)

map_df["Longitude"] = pd.to_numeric(
    map_df["Longitude"],
    errors="coerce"
)

# Remove missing coordinates
map_df = map_df.dropna(
    subset=["Latitude", "Longitude"]
)

# Remove invalid geographical coordinates
map_df = map_df[
    map_df["Latitude"].between(-90, 90) &
    map_df["Longitude"].between(-180, 180)
]

# Select hover information
possible_hover = [
    "Location",
    "Role",
    "Job Title",
    "Company"
]

hover_column = next(
    (
        col for col in possible_hover
        if col in map_df.columns
    ),
    None
)

# Display map
if not map_df.empty:

    fig = px.scatter_map(
        map_df,
        lat="Latitude",
        lon="Longitude",
        hover_name=hover_column,
        zoom=3,
        height=600,
        map_style="open-street-map"
    )

    fig.update_layout(
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

    st.caption(
        f"Showing {len(map_df)} job records "
        "with valid geographical coordinates."
    )

else:

    st.warning(
        "No valid geographical coordinates available."
    )


# --------------------------------------------------
# Location Analysis
# --------------------------------------------------

st.subheader("🏙️ Top Hiring Locations")

if "Location" in jobs_df.columns:

    location_df = (
        jobs_df["Location"]
        .dropna()
        .value_counts()
        .head(15)
        .reset_index()
    )

    location_df.columns = [
        "Location",
        "Jobs"
    ]

    if not location_df.empty:

        fig = px.bar(
            location_df,
            x="Location",
            y="Jobs",
            title="Top Hiring Locations",
            text="Jobs"
        )

        fig.update_layout(
            xaxis_title="Location",
            yaxis_title="Number of Jobs",
            xaxis_tickangle=-45
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

else:

    st.warning(
        "Location column is not available."
    )


# --------------------------------------------------
# Salary by Location
# --------------------------------------------------

st.subheader("💰 Salary by Location")

if (
    "Location" in jobs_df.columns and
    "sal" in jobs_df.columns
):

    salary_data = jobs_df[
        ["Location", "sal"]
    ].copy()

    # Convert salary into numeric values
    salary_data["sal"] = pd.to_numeric(
        salary_data["sal"],
        errors="coerce"
    )

    # Remove missing salary and location values
    salary_data = salary_data.dropna(
        subset=["Location", "sal"]
    )

    # Calculate average salary
    salary_df = (
        salary_data.groupby("Location")["sal"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    if not salary_df.empty:

        fig = px.bar(
            salary_df,
            x="Location",
            y="sal",
            title="Average Salary by Location",
            text_auto=".2s"
        )

        fig.update_layout(
            xaxis_title="Location",
            yaxis_title="Average Salary",
            xaxis_tickangle=-45
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No valid salary information available."
        )

else:

    st.warning(
        "Location or salary column is missing."
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
