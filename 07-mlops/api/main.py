"""API de prediccion de churn (cancelacion de suscriptores).

Sirve un modelo de regresion logistica serializado en model.pkl.
Endpoints:
    GET  /health   -> estado del servicio
    POST /predict  -> prediccion de riesgo de cancelacion
"""
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Ruta relativa al archivo, para que funcione igual en Colab y dentro de Docker
MODEL_PATH = Path(__file__).parent / "model.pkl"
modelo = joblib.load(MODEL_PATH)

app = FastAPI(title="API de Churn - Plataforma de Streaming")


class SuscriptorInput(BaseModel):
    """Datos de entrada de un suscriptor (validados por Pydantic)."""

    meses_suscrito: int = Field(..., ge=0, le=600, description="Meses como suscriptor")
    gasto_mensual: float = Field(..., ge=0, description="Gasto mensual en dolares")
    horas_uso_semanal: float = Field(..., ge=0, le=168, description="Horas de uso por semana")


@app.get("/health")
def health():
    """Verifica que el servicio esta en linea."""
    return {"status": "online"}


@app.post("/predict")
def predict(datos: SuscriptorInput):
    """Predice si el suscriptor cancelara su plan."""
    # DataFrame con los mismos nombres de columnas usados en el entrenamiento
    entrada = pd.DataFrame(
        [[datos.meses_suscrito, datos.gasto_mensual, datos.horas_uso_semanal]],
        columns=["meses_suscrito", "gasto_mensual", "horas_uso_semanal"],
    )
    cancela = int(modelo.predict(entrada)[0])
    return {
        "cancela": cancela,
        "riesgo": "Alto" if cancela == 1 else "Bajo",
    }
