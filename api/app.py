from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
import os


app = FastAPI(title="Adidas Sales Prediction API")


# Cargar modelo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "adidas_pipeline.pkl")

model = joblib.load(MODEL_PATH)


# Root

@app.get("/")
def home():
    return {"message": "API Adidas activa"}


# Predict

@app.post("/predict")
def predict(data: dict):

    # convertir input a dataframe
    df = pd.DataFrame([data])

    # predicción log
    pred_log = model.predict(df)

    # volver a escala real
    pred = np.expm1(pred_log)

    return {
        "prediction_operating_profit": float(pred[0])
    }