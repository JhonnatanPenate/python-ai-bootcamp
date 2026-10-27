# 05 · Big Data

## 01 · PySpark: transacciones
- **Qué hice:** `SparkSession`, carga de CSV con schema explícito, particiones, limpieza, transformaciones, agregaciones y lectura del plan de ejecución (`explain`).
- **Qué aprendí:** Spark es *lazy*; nada se ejecuta hasta una acción, y el plan de ejecución muestra qué va a hacer realmente.

## 02 · Persistencia en MySQL con Docker
- **Qué hice:** escribí el resumen por categoría de Spark en una tabla MySQL que corría en un contenedor Docker, vía JDBC. La contraseña se pide con `getpass`, sin escribirla en el código.
- **Qué aprendí:** conectar un proceso de datos con una base de datos real y manejar credenciales sin exponerlas.

## 03 · Dask vs Pandas + MongoDB Atlas
- **Qué hice:** generé ~3 millones de pedidos en 6 archivos, los procesé de forma secuencial (Pandas) y en paralelo (Dask), filtré por canal digital, guardé los resultados en MongoDB Atlas e hice consultas con filtros, ordenamiento y `$group`.
- **Resultados:** a ese tamaño, Pandas (7.1 s) fue un poco más rápido que Dask (7.6 s).
- **Qué aprendí:** paralelizar tiene un costo; Dask se justifica cuando los datos ya no caben cómodos en memoria.
- **Nota:** la cadena de conexión se reemplazó por `<TU_MONGODB_URI>`.
