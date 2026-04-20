import numpy as np
import joblib

from src.pipeline import load_data, build_pipeline

print("🚀 Iniciando entrenamiento")

# -----------------------------
# 1. CARGA
# -----------------------------
df = load_data("data/Adidas_US_Sales_Datasets.xlsx")

# -----------------------------
# 2. SEPARAR TARGET (FUERA DEL PIPELINE)
# -----------------------------
y = np.log1p(df["Operating Profit"])
X = df.drop(columns=["Operating Profit"])

# -----------------------------
# 3. PIPELINE
# -----------------------------
pipeline = build_pipeline()

# -----------------------------
# 4. ENTRENAMIENTO
# -----------------------------
pipeline.fit(X, y)

print("✅ Modelo entrenado")

# -----------------------------
# 5. GUARDAR MODELO
# -----------------------------
joblib.dump(pipeline, "models/adidas_pipeline.pkl")

print("💾 Modelo guardado en /models")