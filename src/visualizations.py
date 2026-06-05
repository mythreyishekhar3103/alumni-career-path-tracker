import plotly.express as px
import plotly.graph_objects as go


# -----------------------------------
# Bar Chart
# -----------------------------------

def create_bar_chart(
    data,
    x,
    y,
    title="Bar Chart"
):

    fig = px.bar(
        data,
        x=x,
        y=y,
        title=title
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig


# -----------------------------------
# Pie Chart
# -----------------------------------

def create_pie_chart(
    data,
    names,
    values,
    title="Pie Chart"
):

    fig = px.pie(
        data,
        names=names,
        values=values,
        title=title
    )

    return fig


# -----------------------------------
# Histogram
# -----------------------------------

def create_histogram(
    data,
    column,
    title="Distribution"
):

    fig = px.histogram(
        data,
        x=column,
        title=title
    )

    return fig


# -----------------------------------
# Scatter Plot
# -----------------------------------

def create_scatter_plot(
    data,
    x,
    y,
    color=None,
    title="Scatter Plot"
):

    fig = px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        title=title
    )

    return fig


# -----------------------------------
# Line Chart
# -----------------------------------

def create_line_chart(
    data,
    x,
    y,
    title="Line Chart"
):

    fig = px.line(
        data,
        x=x,
        y=y,
        title=title
    )

    return fig


# -----------------------------------
# Salary Distribution
# -----------------------------------

def salary_distribution(
    df,
    salary_column="sal"
):

    fig = px.histogram(
        df,
        x=salary_column,
        title="Salary Distribution"
    )

    return fig


# -----------------------------------
# Experience Distribution
# -----------------------------------

def experience_distribution_chart(
    df,
    exp_column="Experience"
):

    fig = px.histogram(
        df,
        x=exp_column,
        title="Experience Distribution"
    )

    return fig


# -----------------------------------
# Top Locations
# -----------------------------------

def location_chart(
    df,
    location_column="Location"
):

    locations = (
        df[location_column]
        .value_counts()
        .reset_index()
    )

    locations.columns = [
        "Location",
        "Count"
    ]

    fig = px.bar(
        locations,
        x="Location",
        y="Count",
        title="Top Hiring Locations"
    )

    return fig


# -----------------------------------
# Job Category Analysis
# -----------------------------------

def job_category_chart(
    df,
    category_column="Role Category"
):

    categories = (
        df[category_column]
        .value_counts()
        .reset_index()
    )

    categories.columns = [
        "Category",
        "Count"
    ]

    fig = px.bar(
        categories,
        x="Category",
        y="Count",
        title="Job Categories"
    )

    return fig


# -----------------------------------
# Map Visualization
# -----------------------------------

def create_job_map(df):

    if (
        "Latitude" not in df.columns
        or
        "Longitude" not in df.columns
    ):
        return None

    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        hover_name="Location",
        zoom=3,
        height=600
    )

    fig.update_layout(
        mapbox_style="open-street-map"
    )

    return fig


# -----------------------------------
# Skill Frequency Chart
# -----------------------------------

def skill_chart(skill_series):

    skill_df = (
        skill_series
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
        title="Top Skills"
    )

    return fig


# -----------------------------------
# Sankey Diagram
# -----------------------------------

def create_sankey(
    labels,
    source,
    target,
    value
):

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    label=labels
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value
                )
            )
        ]
    )

    fig.update_layout(
        title_text="Career Path Flow",
        font_size=12
    )

    return fig
