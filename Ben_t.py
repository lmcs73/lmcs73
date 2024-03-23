import numpy as np
import pandas as pd
from scipy.linalg import lstsq
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Carregar dados
benihana = pd.read_csv('benihana3.csv')

# Removendo as strings ' minutes' para converter as colunas para numéricas
for col in ['Dining_1', 'Dining_2', 'Dining_3']:
    benihana[col] = benihana[col].str.replace(' minutes', '').astype(int)

# Convertendo 'Opening' para um formato de hora decimal
benihana['Opening'] = pd.to_datetime(benihana['Opening']).dt.hour + pd.to_datetime(benihana['Opening']).dt.minute / 60

# Variáveis explicativas numéricas
numeric_variables = ['advertise', 'B_size', 'Dining_1', 'Dining_2', 'Dining_3', 'Opening']

# Variáveis explicativas categóricas
categorical_variables = ['Campaign', 'Batching_1', 'Batching_2', 'Batching_3']

# Variável dependente
y = benihana['Profit']

# Processamento de variáveis categóricas com OneHotEncoder
column_transformer = ColumnTransformer(
    [('category', OneHotEncoder(handle_unknown='ignore'), categorical_variables)],
    remainder='passthrough'
)

# Transformação das colunas com o ColumnTransformer
X_transformed = column_transformer.fit_transform(benihana)

# Preparar a matriz de design A incluindo um intercepto
A = np.c_[np.ones(X_transformed.shape[0]), X_transformed]

# Resolver a regressão linear
C, _, _, _ = lstsq(A, y, lapack_driver='gelsy')

# Imprimir os coeficientes encontrados
print("Coeficientes:")
feature_names = ['Intercepto'] + list(column_transformer.named_transformers_['category'].get_feature_names_out()) + numeric_variables
for name, coef in zip(feature_names, C):
    print(f"{name}: {coef}")
