import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Adquisición y Definición
housing = fetch_california_housing(as_frame=True)
df = housing.frame

X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']

# División de Datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Estandarización (SOLO X, NO Y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Datos preprocesados y listos para el modelado.")

# Entrenamiento del Bosque Aleatorio
forest_reg = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
forest_reg.fit(X_train_scaled, y_train)

# Predecir sobre el conjunto de prueba (la predicción NO está escalada)
y_pred_forest = forest_reg.predict(X_test_scaled)

r2_forest = r2_score(y_test, y_pred_forest)

print(f"\nR² Score (Precisión): {r2_forest:.3f}")

# Preparación de Datos para Power BI

# Creamos un diccionario con las columnas clave
datos_para_bi = {
    # Coordenadas originales
    'Latitude': X_test['Latitude'].values, 
    'Longitude': X_test['Longitude'].values,

    # Precio Real
    'Precio_Real': y_test.values, 
    
    # Predicción
    'Precio_Predicho': y_pred_forest, 
}

# Creamos el DataFrame final y calculamos el error
df_final_bi = pd.DataFrame(datos_para_bi)
df_final_bi['Error_Absoluto'] = np.abs(df_final_bi['Precio_Real'] - df_final_bi['Precio_Predicho'])

# Exportar el CSV
df_final_bi.to_csv(
    'predicciones_viviendas_bi_FINAL_CORREGIDO.csv', 
    index=False, 
    # El parámetro 'decimal' le dice a Pandas qué carácter usar como decimal
    decimal=',' 
)
print("\n DataFrame EXPORTADO CON ÉXITO: predicciones_viviendas_bi_FINAL_CORREGIDO.csv")