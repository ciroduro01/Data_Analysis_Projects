import pandas as pd
from sklearn.datasets import fetch_california_housing

# 1. Cargar el dataset (Scikit-learn lo descarga si es necesario)
housing = fetch_california_housing(as_frame=True)

# 2. El dataset viene como un objeto de Scikit-learn; lo convertimos a un DataFrame de Pandas.
# Los datos están en 'housing.frame'
df = housing.frame

# 3. Ver las primeras filas
print(df.head())
print(df.info())