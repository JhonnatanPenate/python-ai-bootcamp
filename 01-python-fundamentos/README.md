# 01 · Python fundamentos

## 01 · Pipeline de datos con POO
- **Qué hice:** un pipeline `DataLoader → DataCleaner → DataAnalyst` usando una clase abstracta (`DataComponent`), mixins (`ValidatorMixin`, `LoggerMixin`), `@property` e imputación de nulos. Lo repliqué en un ejercicio final con datos de empleados.
- **Qué aprendí:** separar responsabilidades en clases hace que cada paso se pueda reutilizar y probar por separado, y el polimorfismo permite cambiar el tipo de análisis sin tocar el resto del pipeline.

## 02 · Optimización: profiling, decoradores y NumPy
- **Qué hice:** medí CPU con `cProfile` y RAM con `memory_profiler`, creé un decorador `@monitor_rendimiento` con umbral de alerta, reescribí bucles con broadcasting y fancy indexing de NumPy, y ajusté regresiones con SciPy y statsmodels (OLS).
- **Resultados:** pipeline **4.4x** más rápido en el taller y **35x** en el ejercicio final de logística; regresión múltiple con R² de 0.93.
- **Qué aprendí:** primero se mide y después se optimiza; los bucles de Python puro son el cuello de botella típico.

## 03 · Divvy: series de tiempo y análisis geoespacial
- **Qué hice:** conversión de fechas, duración de viajes, `DatetimeIndex` con resampling diario y semanal, un `GeoDataFrame` con spatial join por zonas y un mapa de calor.
- **Qué aprendí:** cómo trabajar con datos que tienen dimensión de tiempo y de ubicación al mismo tiempo.

## 04 · Visualización: Olympics
- **Qué hice:** EDA del dataset de Juegos Olímpicos y tres visualizaciones: una estática (Matplotlib/Seaborn) y dos interactivas (Plotly, Altair), usando IA para diseñar los prompts de cada gráfico.
- **Qué aprendí:** cada gráfico debe contar una historia concreta; la interactividad solo vale la pena si agrega algo.
