import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_dataset(file_path):
    """
    Load CSV dataset
    """
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """
    Basic data cleaning
    """
    df = df.drop_duplicates()
    df = df.dropna()

    return df


def encode_categorical_columns(df):
    """
    Encode all categorical columns
    """
    encoders = {}

    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_columns:
        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(
            df[col].astype(str)
        )

        encoders[col] = encoder

    return df, encoders


def scale_features(X):
    """
    Scale numerical features
    """
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler


def prepare_career_dataset(
        file_path,
        target_column
):
    """
    Complete preprocessing pipeline
    """

    # Load data
    df = load_dataset(file_path)

    # Clean
    df = clean_data(df)

    # Encode
    df, encoders = encode_categorical_columns(df)

    # Split target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Scale
    X_scaled, scaler = scale_features(X)

    return (
        X_scaled,
        y,
        scaler,
        encoders,
        df
    )
