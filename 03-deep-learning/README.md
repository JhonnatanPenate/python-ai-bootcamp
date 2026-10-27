# 03 · Deep Learning

## 01 · Sandbox de redes neuronales (Breast Cancer Wisconsin)
- **Qué hice:** comparé tres arquitecturas en Keras: minimalista, profunda y optimizada con dropout y EarlyStopping. Analicé las curvas de `val_loss` para detectar en qué epoch empieza el overfitting.
- **Resultados:**

| Modelo | Test accuracy | Parámetros |
|--------|---------------|------------|
| A · Minimalista | **97.4%** | 257 |
| B · Profundo | 95.6% | 4,609 |
| C · Optimizado | 96.5% | 4,609 |

- **Qué aprendí:** más capas no siempre es mejor; con un dataset pequeño, el modelo más simple fue el que mejor generalizó.

## 02 · CNN: Fashion-MNIST
- **Qué hice:** preparé los tensores de imágenes, diseñé y entrené una CNN, y analicé la matriz de confusión desde el punto de vista de negocio (e-commerce de moda).
- **Resultados:** **90%** accuracy en test (97% en entrenamiento, una señal de overfitting). Los errores se concentran en prendas parecidas, como Shirt vs T-shirt o Coat vs Pullover.
- **Qué aprendí:** la métrica global no basta; hay que ver qué clases se confunden y cuánto le cuesta eso al negocio.
