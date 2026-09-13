import pickle

import pandas as pd

from app.core.config import MODEL_PATH


# Load model only once when application starts
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict_diabetes(data):

    input_data = pd.DataFrame([
        {
            "Glucose": data.Glucose,
            "BloodPressure": data.BloodPressure,
            "BMI": data.BMI,
            "DiabetesPedigreeFunction": data.DiabetesPedigreeFunction,
            "Age": data.Age
        }
    ])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        result = "Diabetes detected"
    else:
        result = "No diabetes detected"

    return {
        "prediction": int(prediction),
        "result": result,
        "probability": round(float(probability), 2)
    }