import numpy as np
import pandas as pd
from scipy.linalg import lstsq

# Assuming your CSV is loaded correctly
# Sample data is provided for context, so replace 'benihana3.csv' with your actual file path
benihana = pd.read_csv('benihana3.csv')

# Numeric and categorical variables are correctly identified
numeric_variables = ['advertise', 'B_size', 'Dining_1', 'Dining_2', 'Dining_3', 'Opening']
categorical_variables = ['Campaign', 'Batching_1', 'Batching_2', 'Batching_3']

# Dependent variable
y = benihana['Profit']

# Pre-process categorical variables using one-hot encoding
dummies = pd.get_dummies(benihana[categorical_variables], drop_first=True)

# Concatenate numeric variables and dummies
X = pd.concat([benihana[numeric_variables], dummies], axis=1)

# Ensure all columns in X are numeric, convert if necessary
X = X.apply(pd.to_numeric, errors='coerce')

# Prepare the design matrix A including an intercept
A = np.c_[np.ones(X.shape[0]), X]

# Solve the linear regression
C, residuals, rank, s = lstsq(A, y)

# Print the coefficients
print("Coeficientes:")
for name, coef in zip(['Intercepto'] + X.columns.tolist(), C):
    print(f"{name}: {coef}")
