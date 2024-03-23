import numpy as np
import pandas as pd
from scipy.linalg import lstsq
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Carregar dados
benihana = pd.read_csv('benihana3.csv')

# Variáveis explicativas numéricas
numeric_variables = ['advertise', 'B_size', 'Dining_1', 'Dining_2', 'Dining_3', 'Opening']

# Variáveis explicativas categóricas
categorical_variables = ['Campaign', 'Batching_1', 'Batching_2', 'Batching_3']

# Variável dependente
y = benihana['Profit']

# Garantir que todas as variáveis numéricas são do tipo float
for col in numeric_variables:
    benihana[col] = benihana[col].astype(float)

# Pré-processar variáveis categóricas
# Converter para variáveis dummy
dummies = pd.get_dummies(benihana[categorical_variables], drop_first=True)

# Juntar as variáveis numéricas e dummies
X = pd.concat([benihana[numeric_variables], dummies], axis=1)

# Preparar a matriz de design A incluindo um intercepto
A = np.c_[np.ones(X.shape[0]), X.values]

# Resolver a regressão linear
C, residuals, rank, s = lstsq(A, y)

# Imprimir os coeficientes encontrados
print("Coeficientes:")
for name, coef in zip(['Intercepto'] + X.columns.tolist(), C):
    print(f"{name}: {coef}")
