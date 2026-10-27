# Python & AI Basics Bootcamp — Kodigo

Proyectos y laboratorios que desarrollé durante el bootcamp **Python & AI Basics** de **Kodigo**, Academia de Tecnología Creativa (junio – octubre 2026): desde Python orientado a objetos hasta desplegar un modelo de Machine Learning como API con Docker.

> **EN:** Hands-on notebooks from Kodigo's *Python & AI Basics* bootcamp — data wrangling, classical ML, deep learning, NLP with BERT, big data with PySpark/Dask, testing, and serving a model with FastAPI + Docker.

## Proyectos

| # | Proyecto | Qué hice | Tecnologías |
|---|----------|----------|-------------|
| 01 | [Pipeline de datos con POO](01-python-fundamentos/01_poo_pipeline_datos.ipynb) | Pipeline de carga, limpieza y análisis con clases abstractas, mixins y polimorfismo | Python, pandas |
| 01 | [Optimización y profiling](01-python-fundamentos/02_optimizacion_profiling_decoradores.ipynb) | Detecté cuellos de botella, creé un decorador de rendimiento y vectoricé con NumPy (**35x más rápido**) | cProfile, NumPy, SciPy, statsmodels |
| 01 | [Movilidad urbana Divvy](01-python-fundamentos/03_divvy_series_tiempo_geoespacial.ipynb) | Series de tiempo y análisis geoespacial de viajes en bicicleta | pandas, GeoPandas |
| 01 | [Visualización Olympics](01-python-fundamentos/04_visualizacion_olympics.ipynb) | EDA y tres visualizaciones (estática e interactivas) diseñadas con apoyo de IA | Matplotlib, Plotly, Altair |
| 02 | [Feature engineering + Optuna](02-machine-learning/01_feature_engineering_optuna.ipynb) | Demanda de bicicletas en Seúl: R² de **0.55 → 0.87** con nuevas variables y XGBoost optimizado | scikit-learn, XGBoost, Optuna |
| 02 | [Clustering de países](02-machine-learning/02_clustering_paises.ipynb) | Segmentación de países por indicadores socioeconómicos | scikit-learn (PCA, K-Means, DBSCAN) |
| 02 | [IA ética](02-machine-learning/03_ia_etica_shap_lime.ipynb) | Expliqué un modelo con SHAP y LIME y evalué sesgos entre grupos | XGBoost, SHAP, LIME |
| 03 | [Redes neuronales](03-deep-learning/01_redes_neuronales_sandbox.ipynb) | Comparé 3 arquitecturas y detecté overfitting (mejor: **97.4%** accuracy) | TensorFlow / Keras |
| 03 | [CNN Fashion-MNIST](03-deep-learning/02_cnn_fashion_mnist.ipynb) | Clasificador de ropa (**90%** accuracy) con análisis de errores e impacto de negocio | TensorFlow / Keras |
| 04 | [NLP reseñas Alexa](04-nlp/01_nlp_resenas_alexa.ipynb) | Sentimiento, similitud con embeddings y tópicos (LDA) en 3,150 reseñas | spaCy, TextBlob, gensim |
| 04 | [BERT sentimiento fútbol](04-nlp/02_bert_sentimiento_futbol.ipynb) | Transfer learning con BERT congelando capas base | Hugging Face Transformers |
| 04 | [BERT filtro de spam](04-nlp/03_bert_filtro_spam.ipynb) | Fine-tuning con dataset desbalanceado (**F1 spam 0.93**) | Hugging Face Transformers |
| 05 | [PySpark transacciones](05-big-data/01_pyspark_transacciones.ipynb) | Limpieza, transformación, agregación y plan de ejecución en Spark | PySpark |
| 05 | [Persistencia en MySQL](05-big-data/02_pyspark_persistencia_mysql_docker.ipynb) | Escritura de resultados de Spark a MySQL corriendo en Docker | PySpark, JDBC, MySQL, Docker |
| 05 | [Dask vs Pandas + MongoDB](05-big-data/03_dask_vs_pandas_mongodb.ipynb) | Comparé procesamiento secuencial vs paralelo (3M filas) y consultas en MongoDB Atlas | Dask, pandas, PyMongo |
| 06 | [Calidad de código](06-calidad-de-codigo/01_estructura_git_pytest.ipynb) | Estructura de proyecto, Git, docstrings y pruebas unitarias | Git, pytest |
| 07 | [**MLOps: modelo como API**](07-mlops/) | Modelo de churn servido con FastAPI, validación con Pydantic y contenedor Docker | FastAPI, Pydantic, Docker |

## Estructura

```
python-ai-bootcamp/
├── 01-python-fundamentos/   POO, optimización, series de tiempo, visualización
├── 02-machine-learning/     Feature engineering, clustering, IA explicable
├── 03-deep-learning/        Redes neuronales y CNN
├── 04-nlp/                  NLP clásico y BERT
├── 05-big-data/             PySpark, MySQL, Dask, MongoDB
├── 06-calidad-de-codigo/    Git y pytest
└── 07-mlops/                API FastAPI + Docker
```

## Cómo ver los notebooks

- **En GitHub:** clic en cualquier `.ipynb`; se ven el código y los resultados.
- **En Colab:** `Archivo → Abrir cuaderno → GitHub` y pega la URL del repo.
- La mayoría usa datasets públicos o sintéticos que se cargan desde el propio notebook.
- Los notebooks que usan servicios externos (MongoDB Atlas, MySQL) tienen las credenciales reemplazadas por marcadores como `<TU_MONGODB_URI>`.

## Autor

**Jhonnatan Ezequiel Peñate Serrano** — Estudiante de Ingeniería de Software y Negocios Digitales, ESEN (El Salvador).
