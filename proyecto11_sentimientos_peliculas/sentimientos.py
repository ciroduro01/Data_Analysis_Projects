import pandas as pd
import re 
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import psycopg2
from psycopg2 import Error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import config

# Descargamos Recursos de NLTK
try:
    # Solo necesitamos stopwords
    nltk.download('stopwords', quiet=True) 
except Exception:
    pass

# Cargamos el Dataset
nombre_archivo = 'IMDB_Dataset.csv'
try:
    df = pd.read_csv(nombre_archivo) 
    df.rename(columns={'review': 'text', 'sentiment': 'label'}, inplace=True)
    df['label'] = df['label'].map({'positive': 1, 'negative': 0})
    df = df[['text', 'label']].copy()
    print(f"Dataset cargado. Total de {len(df)} registros.")
except FileNotFoundError:
    print(f"ERROR: Asegúrate de que el archivo '{nombre_archivo}' esté en la carpeta.")
    exit()


# Limpieza de Texto y Tokenización Robusta

stop_words = set(stopwords.words('english')) 

def limpiar_texto(texto):
    if not isinstance(texto, str):
        return ""
        
    # Eliminamos etiquetas HTML
    texto = re.sub(r'<.*?>', ' ', texto) 
    
    # Convertimoa a minúsculas
    texto = texto.lower()
    
    # Eliminamos caracteres no alfabéticos, dejando solo letras y espacios.
    texto = re.sub(r'[^a-z\s]', ' ', texto)
    
    # TOKENIZACIÓN ROBUSTA Usando split()
    # Divide la cadena por espacios en blanco
    tokens = texto.split() 
    
    # Filtramos stopwords y unirse de nuevo
    tokens_filtrados = [word for word in tokens if word not in stop_words and len(word) > 1]
    
    return " ".join(tokens_filtrados)

# Aplicamos la función de limpieza al DataFrame
print("Aplicando limpieza de texto...")
df['texto_limpio'] = df['text'].apply(limpiar_texto)
df = df[df['texto_limpio'] != ''].copy()

print("--- Muestra de Texto Limpio Finalizado ---")
print(df[['text', 'texto_limpio', 'label']].head(3))
print(f"Limpieza finalizada. Registros útiles: {len(df)}")

# Nos preparamos para el Modelado (Dataset Training/Test)

X = df['texto_limpio']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\n--- Preparación para Modelado (Fase 2) ---")
print(f"Tamaño del set de Entrenamiento (X_train): {len(X_train)}")
print(f"Tamaño del set de Prueba (X_test): {len(X_test)}")

print("\n--- FASE 2: Vectorización y Entrenamiento ---")

# Creamos el Vectorizador TF-IDF
# max_features=5000: Limita el vocabulario a las 5000 palabras más frecuentes, lo cual reduce el ruido y mejora la velocidad.
vectorizer = TfidfVectorizer(max_features=5000)

# Ajustamos y Transformamos (Fit & Transform) el set de entrenamiento (X_train)
# El ajuste solo se hace en los datos de entrenamiento para evitar el "data leakage"
X_train_vectorized = vectorizer.fit_transform(X_train)
print("Vectorizador TF-IDF ajustado.")
print(f"Diccionario creado con {len(vectorizer.get_feature_names_out())} características.")


# Transformamos el set de prueba (X_test)
# Solo se usa la función 'transform' (sin 'fit')
X_test_vectorized = vectorizer.transform(X_test)


# Entrenamos el Modelo de Regresión Logística
# Es un modelo muy eficiente para clasificaciones de texto binarias
modelo_sentimiento = LogisticRegression(max_iter=1000, random_state=42)
modelo_sentimiento.fit(X_train_vectorized, y_train)
print("Modelo de Regresión Logística entrenado con éxito.")


# Predicción y Evaluación
y_pred = modelo_sentimiento.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, y_pred)


print("\n--- FASE 3: Evaluación del Modelo ---")
print(f"Precisión (Accuracy) del Modelo: {accuracy:.4f}")
print("\nReporte de Clasificación:")
# El reporte muestra Precision, Recall y F1-score para 0 (Negativo) y 1 (Positivo)
print(classification_report(y_test, y_pred, target_names=['Negativo (0)', 'Positivo (1)']))


# Prueba en una Nueva Reseña
def predecir_sentimiento(texto_nuevo):
    texto_limpio = limpiar_texto(texto_nuevo) # Usamos la función de limpieza anterior
    
    # Vectorizar el texto nuevo (Solo 'transform')
    texto_vectorizado = vectorizer.transform([texto_limpio])
    
    # Predecir
    prediccion = modelo_sentimiento.predict(texto_vectorizado)[0]
    
    # Mostrar resultado
    sentimiento = "Positivo" if prediccion == 1 else "Negativo"
    
    print(f"\nReseña: '{texto_nuevo}'")
    print(f"Predicción del Modelo: {sentimiento}")

# Ejemplos de prueba:
predecir_sentimiento("This movie was an absolute disaster, completely boring and a waste of time.")
predecir_sentimiento("A cinematic masterpiece! The acting and directing were flawless.")
# Creando un DataFrame con los resultados para Power BI
df_resultados_bi = pd.DataFrame({
    'Texto_Original': X_test.tolist(),
    'Sentimiento_Predicho': y_pred.tolist(), # 1 o 0
    'Probabilidad_Positiva': modelo_sentimiento.predict_proba(X_test_vectorized)[:, 1].tolist()
})

# Mapeo de etiqueta numérica a texto para facilitar la visualización
df_resultados_bi['Etiqueta_Sentimiento'] = df_resultados_bi['Sentimiento_Predicho'].map({1: 'Positivo', 0: 'Negativo'})

# Exportación
df_resultados_bi.to_csv('sentimientos_predichos_bi.csv', index=False)
print("\nExportación para Power BI lista: 'sentimientos_predichos_bi.csv'")       

print("\n--- Conexión y Carga a PostgreSQL ---")

# Obtener las probabilidades (0 a 1) para el set de prueba (X_test)
# predict_proba[0] = Negativo, [1] = Positivo
y_proba = modelo_sentimiento.predict_proba(X_test_vectorized)[:, 1] 

# Combinar resultados: texto limpio, predicción (True/False) y probabilidad
resultados = pd.DataFrame({
    'texto_original': X_test.tolist(),
    'prediccion': y_pred.tolist(),
    'probabilidad': y_proba.tolist()
})

# Seleccionamos solo 100 resultados para la inserción de prueba
resultados_muestra = resultados.sample(n=100, random_state=42)

def insertar_resultados():
    conn = None
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS, port=config.DB_PORT)
        cursor = conn.cursor()
        
        # Definición del comando SQL INSERT
        insert_query = """
        INSERT INTO resultados_sentimientos (texto_original, sentimiento_predicho, probabilidad_positiva)
        VALUES (%s, %s, %s);
        """
        
        # Preparación de los datos para la inserción
        datos_a_insertar = [
            (row['texto_original'], bool(row['prediccion']), row['probabilidad']) # Usamos el flotante de Python directamente
            for index, row in resultados_muestra.iterrows()
        ]

        # Ejecución del comando
        cursor.executemany(insert_query, datos_a_insertar)
        conn.commit()
        print(f"Éxito: Se insertaron {len(datos_a_insertar)} resultados en la tabla 'resultados_sentimientos'.")
        
    except Error as e:
        print(f"Error de PostgreSQL: {e}")
        if conn:
            conn.rollback() # Revierte la transacción en caso de error
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexión a PostgreSQL cerrada.")

insertar_resultados()

print("\n--- FASE 4: Visualización de Resultados (Matplotlib/Seaborn) ---")

# Generación de la Matriz de Confusión
# cm_results contiene: [[TN, FP], [FN, TP]]
cm_results = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(
    cm_results, 
    annot=True, 
    fmt='d', 
    cmap='Blues', 
    xticklabels=['Negativo (0)', 'Positivo (1)'], 
    yticklabels=['Negativo (0)', 'Positivo (1)']
)
plt.title('Matriz de Confusión')
plt.ylabel('Etiqueta Real')
plt.xlabel('Predicción del Modelo')
plt.show() # Muestra la primera figura

# Distribución de Sentimientos Predichos
# Contamos cuántas predicciones fueron 0 (Negativo) y 1 (Positivo)
distribucion = pd.Series(y_pred).value_counts().sort_index()
# Definir un mapa de colores que asocie el valor numérico (0, 1) con el color, asumiendo 0 (Negativo) = 'red' y 1 (Positivo) = 'green'.
color_map_sentimiento = {0: 'red', 1: 'green'}

plt.figure(figsize=(6, 4))
sns.barplot(
    x=distribucion.index, 
    y=distribucion.values, 
    # Le decimos a Seaborn qué variable define el color (hue)
    hue=distribucion.index, 
    # Usamos el mapa de colores específico
    palette=color_map_sentimiento, 
    legend=False
)
plt.title('Distribución de Sentimientos Predichos (Set de Prueba)')
plt.xlabel('Sentimiento (0: Negativo, 1: Positivo)')
plt.ylabel('Número de Reseñas')
plt.xticks([0, 1], ['Negativo', 'Positivo'])
plt.show() # Muestra la segunda figura

print("Visualización de la Matriz de Confusión y la Distribución de Sentimientos generada.")