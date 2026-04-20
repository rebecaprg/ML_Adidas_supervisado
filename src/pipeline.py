import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor


# -----------------------------
# 1. CARGA DE DATOS
# -----------------------------
def load_data(path):
    df = pd.read_excel(path, sheet_name="Data Sales Adidas", header=4)
    df.columns = df.columns.str.strip()
    return df


# -----------------------------
# 2. FEATURE ENGINEERING
# -----------------------------
class FeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        df = X.copy()

        # -----------------
        # FEATURES TIEMPO
        # -----------------
        df["Invoice Date"] = pd.to_datetime(df["Invoice Date"])

        df["year"] = df["Invoice Date"].dt.year
        df["month"] = df["Invoice Date"].dt.month
        df["dayofweek"] = df["Invoice Date"].dt.dayofweek

        df["quarter"] = (df["month"] - 1) // 3 + 1
        df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)
        df["holiday_season"] = df["month"].isin([11, 12]).astype(int)

        df = df.drop("Invoice Date", axis=1)

        # -----------------
        # FEATURES NUMÉRICAS
        # -----------------
        df["Price_x_Units"] = df["Price per Unit"] * df["Units Sold"]
        df["log_units"] = np.log1p(df["Units Sold"])

        # -----------------
        # CATEGÓRICAS (ONE HOT)
        # -----------------
        categorical_cols = [
            "Retailer",
            "Region",
            "State",
            "City",
            "Product",
            "Sales Method"
        ]

        df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

        return df


# -----------------------------
# 3. PIPELINE FINAL
# -----------------------------
def build_pipeline():

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    pipeline = Pipeline(steps=[
        ("features", FeatureEngineer()),
        ("model", model)
    ])

    return pipeline