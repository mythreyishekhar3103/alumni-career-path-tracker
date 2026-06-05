import pandas as pd


# -----------------------------
# General KPIs
# -----------------------------

def get_total_records(df):
    return len(df)


def get_total_columns(df):
    return len(df.columns)


def get_missing_values(df):
    return df.isnull().sum().sum()


# -----------------------------
# Job Analytics
# -----------------------------

def get_total_jobs(df):
    return len(df)


def get_average_salary(df, salary_column="sal"):
    if salary_column in df.columns:
        return round(df[salary_column].mean(), 2)
    return 0


def get_max_salary(df, salary_column="sal"):
    if salary_column in df.columns:
        return df[salary_column].max()
    return 0


def get_min_salary(df, salary_column="sal"):
    if salary_column in df.columns:
        return df[salary_column].min()
    return 0


# -----------------------------
# Recruiter Analytics
# -----------------------------

def top_recruiters(df, company_column="Company", top_n=10):
    
    if company_column in df.columns:
        return (
            df[company_column]
            .value_counts()
            .head(top_n)
        )

    return pd.Series()


# -----------------------------
# Location Analytics
# -----------------------------

def top_locations(df, location_column="Location", top_n=10):

    if location_column in df.columns:
        return (
            df[location_column]
            .value_counts()
            .head(top_n)
        )

    return pd.Series()


# -----------------------------
# Skill Analytics
# -----------------------------

def skill_frequency(df, skill_column="Skills"):

    if skill_column not in df.columns:
        return pd.Series()

    skills = []

    for row in df[skill_column].dropna():

        skill_list = str(row).split(",")

        for skill in skill_list:
            skills.append(skill.strip())

    return pd.Series(skills).value_counts()


# -----------------------------
# Experience Analytics
# -----------------------------

def experience_distribution(
    df,
    exp_column="Experience"
):

    if exp_column in df.columns:
        return df[exp_column].value_counts()

    return pd.Series()


# -----------------------------
# Career Recommendation Analytics
# -----------------------------

def top_career_recommendations(
        df,
        target_column="Primary_Career_Recommendation",
        top_n=10
):

    if target_column in df.columns:

        return (
            df[target_column]
            .value_counts()
            .head(top_n)
        )

    return pd.Series()


# -----------------------------
# Dataset Summary
# -----------------------------

def dataset_summary(df):

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }

    return summary
