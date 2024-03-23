import numpy as np
import pandas as pd
from scipy.linalg import lstsq

# Step 1: Load the dataset
benihana = pd.read_csv('benihana3.csv')

# Step 2: Define numeric and categorical variables
numeric_variables = ['advertise', 'B_size', 'Dining_1', 'Dining_2', 'Dining_3', 'Opening']
categorical_variables = ['Campaign', 'Batching_1', 'Batching_2', 'Batching_3']

# Dependent variable
y = benihana['Profit']

# Step 3: One-hot encode categorical variables
dummies = pd.get_dummies(benihana[categorical_variables], drop_first=True)

# Step 4: Combine numeric and encoded categorical variables
X = pd.concat([benihana[numeric_variables], dummies], axis=1)

# Step 5: Prepare the design matrix A including an intercept
A = np.c_[np.ones(X.shape[0]), X]

# Step 6: Solve the linear regression problem
C, residuals, rank, s = lstsq(A, y)

# Step 7: Print the coefficients
print("Coefficients:")
for name, coef in zip(['Intercept'] + X.columns.tolist(), C):
    print(f"{name}: {coef}")
