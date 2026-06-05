import pandas as pd
import streamlit as st


# ----------------------------------
# Load Dataset
# ----------------------------------

@st.cache_data
def load_data(file_path):
    """
    Load CSV file
    """
    return pd.read_csv(file_path)


# ----------------------------------
# Format Currency
# ----------------------------------

def format_salary(value):
    """
    Format salary values
    """

    try:
        return f"₹ {value:,.0f}"
    except:
        return "N/A"


# ----------------------------------
# Convert Large Numbers
# ----------------------------------

def format_number(num):

    if num >= 1000000:
        return f"{num/1000000:.1f}M"

    elif num >= 1000:
        return f"{num/1000:.1f}K"

    return str(num)


# ----------------------------------
# Dataset Information
# ----------------------------------

def dataset_info(df):

    info = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum()
    }

    return info


# ----------------------------------
# Search Dataset
# ----------------------------------

def search_dataframe(df, keyword):

    if keyword:

        mask = df.astype(str).apply(
            lambda col:
            col.str.contains(
                keyword,
                case=False,
                na=False
            )
        ).any(axis=1)

        return df[mask]

    return df


# ----------------------------------
# Top N Records
# ----------------------------------

def top_n(df, column, n=10):

    return (
        df[column]
        .value_counts()
        .head(n)
    )


# ----------------------------------
# Safe Column Check
# ----------------------------------

def column_exists(df, column):

    return column in df.columns


# ----------------------------------
# Display KPI Card
# ----------------------------------

def show_metric(
        label,
        value,
        delta=None
):

    st.metric(
        label=label,
        value=value,
        delta=delta
    )


# ----------------------------------
# Missing Value Summary
# ----------------------------------

def missing_values_report(df):

    return (
        df.isnull()
        .sum()
        .sort_values(
            ascending=False
        )
    )


# ----------------------------------
# Download Data
# ----------------------------------

def convert_to_csv(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")
