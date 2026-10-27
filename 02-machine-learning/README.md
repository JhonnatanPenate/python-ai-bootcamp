# 02 · Machine Learning

## 01 · Feature engineering + Optuna (Seoul Bike Sharing)
- **Qué hice:** un modelo baseline para predecir bicicletas rentadas por hora; apliqué transformación logarítmica, winsorization de outliers (`rainfall`), target encoding y variables cíclicas (seno/coseno); y optimicé XGBoost con Optuna.
- **Resultados (R²):** baseline 0.55 → con feature engineering 0.64 → XGBoost 0.86 → XGBoost optimizado **0.87**.
- **Qué aprendí:** buenas variables mejoran el modelo antes de tocar hiperparámetros, y el salto más grande vino de cambiar de modelo.

## 02 · Clustering de países (Country Data)
- **Qué hice:** preprocesamiento con pipeline (escalado), PCA para reducir dimensiones, K-Means (K = 3 por el método del codo y el silhouette score), comparación con DBSCAN y perfilado de clusters con heatmap.
- **Qué aprendí:** en aprendizaje no supervisado no hay "respuesta correcta"; el valor está en interpretar cada grupo.

## 03 · IA ética: SHAP y LIME
- **Qué hice:** entrené un clasificador XGBoost (accuracy 0.70, F1 0.65), lo expliqué globalmente con SHAP y caso por caso con SHAP waterfall y LIME, y evalué si trataba distinto a distintos grupos sensibles.
- **Qué aprendí:** un modelo con buena métrica puede apoyarse en variables sensibles; explicar las predicciones es parte de construir el modelo, no un extra.
