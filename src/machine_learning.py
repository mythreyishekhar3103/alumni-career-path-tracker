import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# ---------------------------------------------------
# Train Career Prediction Model
# ---------------------------------------------------

def train_career_model(
        dataset_path,
        target_column
):

    # Create models folder
    os.makedirs("models", exist_ok=True)

    # Load data
    df = pd.read_csv(dataset_path)

    # Clean data
    df = df.dropna()
    df = df.drop_duplicates()

    # Features
    X = df.drop(columns=[target_column])

    # Keep numerical columns only
    X = X.select_dtypes(
        include=["int64", "float64"]
    )

    # Target
    y = df[target_column]

    # Encode target
    label_encoder = LabelEncoder()

    y_encoded = label_encoder.fit_transform(y)

    # Scale features
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y_encoded,
        test_size=0.2,
        random_state=42
    )

    # Model
    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    # Save models
    joblib.dump(
        model,
        "models/career_predictor.pkl"
    )

    joblib.dump(
        scaler,
        "models/scaler.pkl"
    )

    joblib.dump(
        label_encoder,
        "models/label_encoder.pkl"
    )

    return accuracy


# ---------------------------------------------------
# Load Models
# ---------------------------------------------------

def load_models():

    model = joblib.load(
        "models/career_predictor.pkl"
    )

    scaler = joblib.load(
        "models/scaler.pkl"
    )

    label_encoder = joblib.load(
        "models/label_encoder.pkl"
    )

    return model, scaler, label_encoder


# ---------------------------------------------------
# Career Prediction
# ---------------------------------------------------

def predict_career(user_input):

    model, scaler, label_encoder = load_models()

    scaled_input = scaler.transform(
        [user_input]
    )

    prediction = model.predict(
        scaled_input
    )

    career = label_encoder.inverse_transform(
        prediction
    )

    return career[0]


# ---------------------------------------------------
# Feature Importance
# ---------------------------------------------------

def get_feature_importance(
        model,
        feature_names
):

    importance = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    return importance
