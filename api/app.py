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

    # predicción 
    pred = model.predict(df)
    prediction = float(pred[0])

    # Interpretación para negocio
    if prediction < 20:
        level = "bajo"
        insight = "Rentabilidad baja"
        recommendations = [
            "Revisar precio del producto",
            "Reducir costes o mejorar margen",
            "Analizar canal de venta"
        ]

    elif prediction < 50:
        level = "medio"
        insight = "Rentabilidad media"
        recommendations = [
            "Optimizar campañas de marketing",
            "Mejorar mix de productos",
            "Aumentar eficiencia en ventas"
        ]

    else:
        level = "alto"
        insight = "Alta rentabilidad"
        recommendations = [
            "Escalar este tipo de ventas",
            "Invertir más en este segmento",
            "Replicar estrategia en otras regiones"
        ]

    return {
        "prediction_operating_profit": prediction,
        "level": level,
        "insight": insight,
        "recommendations": recommendations
    }