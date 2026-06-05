import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv("data/career_recommendation_dataset.csv")

# Remove missing values
df = df.dropna()

# Target Column
target_column = "Primary_Career_Recommendation"

# Select Numerical Features
X = df.select_dtypes(include=["int64", "float64"])

# Remove target if numeric
if target_column in X.columns:
    X = X.drop(columns=[target_column])

# Target Variable
y = df[target_column]

# Encode Target
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Scale Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

# Model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)

# Train
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.4f}")
print(classification_report(y_test, predictions))

# Save Artifacts
joblib.dump(model, "models/career_predictor.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model Saved Successfully!")
