import joblib

model = joblib.load("models/career_predictor.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


def predict_career(user_input):
    
    scaled_input = scaler.transform([user_input])

    prediction = model.predict(scaled_input)

    career = label_encoder.inverse_transform(prediction)

    return career[0]
