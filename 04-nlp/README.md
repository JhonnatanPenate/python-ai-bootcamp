# 04 · NLP

## 01 · Reseñas de Alexa: sentimiento, similitud y tópicos
- **Qué hice:** limpié 3,150 reseñas reales, clasifiqué el sentimiento con TextBlob, busqué las reseñas más parecidas a una "reseña ideal" con embeddings de spaCy, y apliqué LDA (gensim) para encontrar los temas de las reseñas negativas, con nubes de palabras.
- **Qué aprendí:** el pipeline clásico de NLP: limpieza → representación → modelo → interpretación.

## 02 · BERT: sentimiento en tweets de fútbol
- **Qué hice:** transfer learning con BERT de Hugging Face: tokenización, congelado de las capas base y entrenamiento solo del clasificador, con `Trainer`.
- **Resultados:** 43% accuracy en 3 clases. Con las capas base congeladas y pocos datos, el modelo aprende poco; el siguiente paso sería descongelar las últimas capas.
- **Qué aprendí:** cómo funciona el transfer learning y sus límites cuando casi todo el modelo queda congelado.

## 03 · BERT: filtro de spam
- **Qué hice:** fine-tuning de BERT para detectar spam en un dataset desbalanceado, midiendo precisión y F1 de la clase spam y no solo accuracy.
- **Resultados:** accuracy 92.9%, precisión spam 0.91, **F1 spam 0.93**.
- **Qué aprendí:** con clases desbalanceadas, accuracy engaña; hay que medir la clase que importa.
