import numpy as np
import joblib

from src.pipeline import load_data, build_pipeline

print("Iniciando entrenamiento")


# 1. Cargar datos

df = load_data("data/Adidas_US_Sales_Datasets.xlsx")


# 2. Separar target 

y = np.log1p(df["Operating Profit"])
X = df.drop(columns=["Operating Profit"])


# 3. Pipeline

pipeline = build_pipeline()


# 4. Entrenamiento 
pipeline.fit(X, y)

print("Modelo entrenado")


# 5. Guardar modelo 
joblib.dump(pipeline, "models/adidas_pipeline.pkl")

print("Modelo guardado")