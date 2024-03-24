import numpy as np
import pandas as pd
from scipy.linalg import lstsq

# Load the data
benihana = pd.read_csv('benihana3.csv')

# Numeric variables
numeric_variables = ['advertise', 'B_size', 'Dining_1', 'Dining_2', 'Dining_3', 'Opening']

# Categorical variables for one-hot encoding
categorical_variables = ['Campaign', 'Batching_1', 'Batching_2', 'Batching_3']

# Dependent variable
y = benihana['Profit']

# Pre-process categorical variables using one-hot encoding
for category in categorical_variables:
    # Make sure all categories including '4shareatable' are considered
    all_categories = benihana[category].unique().tolist()
    if '4shareatable' not in all_categories:
        all_categories.append('4shareatable')
    benihana[category] = pd.Categorical(benihana[category], categories=all_categories)

dummies = pd.get_dummies(benihana[categorical_variables], drop_first=True)

# Combine numeric variables and dummies
X = pd.concat([benihana[numeric_variables], dummies], axis=1)

# Ensure all columns in X are numeric and handle NaNs
X = X.apply(pd.to_numeric, errors='coerce').fillna(0)

# Prepare the design matrix A including an intercept
A = np.c_[np.ones(X.shape[0]), X]

# Ensure A and y are of type float64 to avoid dtype issues
A = np.asarray(A, dtype=np.float64)
y = np.asarray(y, dtype=np.float64)

# Perform the linear regression
C, residuals, rank, s = lstsq(A, y)

# Print the coefficients found
print("Coefficients:")
for name, coef in zip(['Intercept'] + X.columns.tolist(), C):
    print(f"{name}: {coef}")
