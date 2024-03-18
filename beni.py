import pandas as pd
import numpy as np
from scipy.linalg import lstsq

# Carrega o dataset
#benihana = pd.read_csv('benihana2.csv')
benihana = pd.read_csv('benihana2.csv', encoding='latin1')

# Lista de variáveis numéricas
numeric_variables = ['advertise', 'B_size', 'Dining_1', 'Dining_2', 'Dining_3', 'Opening']

# Lista de variáveis categóricas para One-Hot Encoding
categorical_variables = ['Campaign', 'Batching_1', 'Batching_2', 'Batching_3']

# Aplica One-Hot Encoding às variáveis categóricas
dummies = pd.get_dummies(benihana[categorical_variables])

# Concatena variáveis numéricas e dummies (categóricas tratadas)
X = pd.concat([benihana[numeric_variables], dummies], axis=1)

# Coluna alvo (y) é o Profit
y = benihana['Profit']

# Realiza a regressão linear
C, _, _, _ = lstsq(X, y)

# Imprime os coeficientes
print("Coeficientes: ", C)

# Exemplo de como prever o Profit com os coeficientes obtidos
# Nota: 'example_input' deve ser alterado para conter os valores de entrada desejados, no mesmo formato que X
example_input = np.array([50, 300, 60, 65, 70, 330, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])  # Exemplo de input
predicted_profit = np.dot(C, example_input)
print("Lucro previsto: ", predicted_profit)
