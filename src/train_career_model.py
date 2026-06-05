import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create models directory if not exists
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/career_recommendation_dataset.csv")

# Remove missing values
df = df.dropna()

# Target column
TARGET = "Primary_Career_Recommendation"

# Check target column exists
if TARGET not in df.columns:
    raise ValueError(
        f"Target column '{TARGET}' not found.\n"
        f"Available columns:\n{list(df.columns)}"
    )

# Features
X = df.drop(columns=[TARGET])

# Keep only numerical columns
X = X.select_dtypes(include=["int64", "float64"])

# Target
y = df[TARGET]

# Encode target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 50)
print("Career Prediction Model")
print("=" * 50)
print(f"Accuracy: {accuracy:.4f}")

# Save files
joblib.dump(model, "models/career_predictor.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")

print("\nFiles Saved Successfully:")
print("models/career_predictor.pkl")
print("models/scaler.pkl")
print("models/label_encoder.pkl")
