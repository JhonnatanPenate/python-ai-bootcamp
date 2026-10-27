"""Entrena el modelo de churn y lo guarda en model.pkl.

Mismo codigo que la Fase 1 del notebook 01_laboratorio_mlops.ipynb
(dataset sintetico con semilla fija, asi el resultado es reproducible).
Uso: python train_model.py
"""
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

np.random.seed(7)
n = 500

meses_suscrito = np.random.randint(1, 48, n)
gasto_mensual = np.random.uniform(5, 60, n)
horas_uso_semanal = np.random.uniform(0, 30, n)

# Regla simulada: menos uso y menos antiguedad aumentan la probabilidad de cancelar
score = (horas_uso_semanal * -0.15) + (meses_suscrito * -0.05) + (gasto_mensual * 0.02) + np.random.normal(0, 1.0, n)
cancela = (score > score.mean()).astype(int)

df = pd.DataFrame({
    "meses_suscrito": meses_suscrito,
    "gasto_mensual": gasto_mensual,
    "horas_uso_semanal": horas_uso_semanal,
    "cancela": cancela,
})

X = df[["meses_suscrito", "gasto_mensual", "horas_uso_semanal"]]
y = df["cancela"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)
print("Precision en test:", modelo.score(X_test, y_test))

joblib.dump(modelo, Path(__file__).parent / "model.pkl")
print("model.pkl guardado")
