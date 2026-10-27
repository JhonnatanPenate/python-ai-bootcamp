# 07 · MLOps: del modelo a una API en Docker

Proyecto final del bootcamp: tomar un modelo entrenado y servirlo como un servicio que cualquier aplicación pueda consumir.

## Qué hice
1. **Modelo:** regresión logística que predice si un suscriptor de streaming cancelará su plan (churn); precisión en test de 0.86.
2. **Serialización:** guardé el modelo con `joblib` (`model.pkl`).
3. **API con FastAPI:**
   - `GET /health` → estado del servicio
   - `POST /predict` → `{"cancela": 0|1, "riesgo": "Bajo"|"Alto"}`
   - Validación de entrada con Pydantic (tipos y rangos); los datos inválidos devuelven `422`.
4. **Docker:** imagen `python:3.13-slim`, dependencias con versiones fijas y capas ordenadas para aprovechar la caché.

## Archivos

```
07-mlops/
├── 01_laboratorio_mlops.ipynb   notebook completo (entrenamiento → API → Docker)
└── api/
    ├── main.py                  API FastAPI
    ├── train_model.py           reentrena y genera model.pkl
    ├── model.pkl                modelo serializado
    ├── requirements.txt         dependencias con versiones fijas
    └── Dockerfile
```

## Cómo correrlo

```bash
cd 07-mlops/api
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

Abre http://localhost:8000/docs y prueba `/predict` con:

```json
{"meses_suscrito": 2, "gasto_mensual": 55.0, "horas_uso_semanal": 1.0}
```

Respuesta esperada: `{"cancela": 1, "riesgo": "Alto"}`.

## Qué aprendí
- Un modelo solo es útil cuando otros sistemas lo pueden consumir.
- La validación de entrada protege al modelo de datos que no tienen sentido.
- Fijar versiones evita que el modelo falle al cargarse en otro entorno.
