import numpy as np
import pandas as pd
from scipy.linalg import lstsq

# Carregar dados
benihana = pd.read_csv('benihana3.csv')

# Variáveis explicativas numéricas
numeric_variables = ['advertise', 'B_size', 'Dining_1', 'Dining_2', 'Dining_3', 'Opening']

# Variáveis explicativas categóricas
categorical_variables = ['Campaign', 'Batching_1', 'Batching_2', 'Batching_3']

# Variável dependente
y = benihana['Profit']

# Pré-processar variáveis categóricas usando one-hot encoding
dummies = pd.get_dummies(benihana[categorical_variables], drop_first=True)

# Juntar as variáveis numéricas e dummies
X = pd.concat([benihana[numeric_variables], dummies], axis=1)

# Verificar se todas as colunas de X são numéricas, caso contrário, converter para numérico ou tratar
# Isso é mais uma medida de precaução, dado que a abordagem anterior já deve garantir que X seja totalmente numérico

# Preparar a matriz de design A incluindo um intercepto
A = np.c_[np.ones(X.shape[0]), X]

# Resolver a regressão linear
C, residuals, rank, s = lstsq(A, y)

# Imprimir os coeficientes encontrados
print("Coeficientes:")
for name, coef in zip(['Intercepto'] + X.columns.tolist(), C):
    print(f"{name}: {coef}")
