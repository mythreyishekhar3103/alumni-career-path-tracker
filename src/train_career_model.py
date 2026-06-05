import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# -----------------------------------------
# Load Dataset
# -----------------------------------------

df = pd.read_csv("data/jobss.csv")

# -----------------------------------------
# Clean Data
# -----------------------------------------

df = df.dropna(
    subset=[
        "Job Experience Required",
        "Role Category",
        "Industry",
        "Location",
        "sal"
    ]
)

# -----------------------------------------
# Experience Extraction
# -----------------------------------------

def get_exp(exp):

    try:

        exp = str(exp)

        if "-" in exp:

            return int(
                exp.split("-")[0].strip()
            )

        return 0

    except:

        return 0

df["Experience"] = df[
    "Job Experience Required"
].apply(get_exp)

# -----------------------------------------
# Label Encoding
# -----------------------------------------

role_encoder = LabelEncoder()
industry_encoder = LabelEncoder()
location_encoder = LabelEncoder()

df["Role Category"] = role_encoder.fit_transform(
    df["Role Category"]
)

df["Industry"] = industry_encoder.fit_transform(
    df["Industry"]
)

df["Location"] = location_encoder.fit_transform(
    df["Location"]
)

# -----------------------------------------
# Features
# -----------------------------------------

X = df[
    [
        "Experience",
        "Role Category",
        "Industry",
        "Location"
    ]
]

y = df["sal"]

# -----------------------------------------
# Split
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------------
# Model
# -----------------------------------------

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

pred = model.predict(X_test)

print(
    "R2 Score:",
    r2_score(
        y_test,
        pred
    )
)

# -----------------------------------------
# Save
# -----------------------------------------

os.makedirs(
    "models",
    exist_ok=True
)

joblib.dump(
    model,
    "models/salary_predictor.pkl"
)

joblib.dump(
    role_encoder,
    "models/role_encoder.pkl"
)

joblib.dump(
    industry_encoder,
    "models/industry_encoder.pkl"
)

joblib.dump(
    location_encoder,
    "models/location_encoder.pkl"
)

print("Model Saved Successfully")
