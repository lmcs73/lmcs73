import numpy as np
import pandas as pd
from scipy.linalg import lstsq

# Carregar dados
benihana = pd.read_csv('benihana2.csv')
x = benihana['advertise'].values
y = benihana['B_size'].values
z = benihana['Profit'].values

# Preparar dados para regressão
data = np.c_[x, y, np.ones(x.shape)]
target = z

# Calcular coeficientes da regressão
C, _, _, _ = lstsq(data, target)

# Coeficientes
print(f"Coeficientes: {C}")

# Função para calcular o lucro esperado
def calcular_lucro(advertise, b_size, coeficientes):
    return coeficientes[0] * advertise + coeficientes[1] * b_size + coeficientes[2]

# Exemplo de uso
advertise_teste = 5
b_size_teste = 10
lucro_esperado = calcular_lucro(advertise_teste, b_size_teste, C) 
print(f"Lucro esperado para advertise={advertise_teste} e B_size={b_size_teste}: {lucro_esperado}")
