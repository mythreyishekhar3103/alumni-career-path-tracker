import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# -------------------------------
# 1. Load dataset
# -------------------------------
DATA_PATH = "data/salary.csv"   # change if your file name differs

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print(df.head())


# -------------------------------
# 2. Data Preprocessing
# -------------------------------
# Example assumption: dataset has columns like:
# YearsExperience -> input
# Salary -> target

if "YearsExperience" not in df.columns or "Salary" not in df.columns:
    raise ValueError("Dataset must contain 'YearsExperience' and 'Salary' columns")

# Handle missing values
df = df.dropna()

X = df[["YearsExperience"]]
y = df["Salary"]


# -------------------------------
# 3. Train-test split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -------------------------------
# 4. Model training
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

print("Model training completed!")


# -------------------------------
# 5. Evaluation
# -------------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)


# -------------------------------
# 6. Save model (.pkl)
# -------------------------------
os.makedirs("models", exist_ok=True)

MODEL_PATH = "models/salary_predictor.pkl"
joblib.dump(model, MODEL_PATH)

print(f"\nModel saved successfully at: {MODEL_PATH}")
