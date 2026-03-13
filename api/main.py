from fastapi import FastAPI
import joblib
import numpy as np  
import os


app = FastAPI(title="Customer Churn Prediction API")

#load trained Random forest Model

model_path = "models/churn_model.pkl"

model = joblib.load(model_path)

@app.get("/predict")

def home():
    return {"message": "Welcome to the Customer Churn Prediction API! Use the /predict endpoint to get predictions."}


#prediction route
@app.post("/predict")

def predict_churn(data: dict):

    #covert input data to numpy array

    features = np.array([[
        data["industry"],
        data["subscription_type"],
        data["country"],
        data["usage_frequency"],
        data["login_activity"],
        data["support_tickets"],
        data["monthly_spend"],
        data["payment_history"],
        data["engagement_score"],
        data["support_ratio"]

    ]])

    prediction = model.predict(features)

    if prediction == 1:
        return {"churn_prediction": "Customer is likely to churn"}
    else:
        return {"churn_prediction": "Customer is likely to stay"}