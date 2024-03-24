import numpy as np
import pandas as pd
from scipy.linalg import lstsq

# Load the data
benihana = pd.read_csv('benihana3.csv')

# Numeric variables
numeric_variables = ['advertise', 'B_size', 'Dining_1', 'Dining_2', 'Dining_3', 'Opening']

# Categorical variables for one-hot encoding
categorical_variables = ['Campaign', 'Batching_1', 'Batching_2', 'Batching_3']
batching_categories = ['SemBatch', '4shareatable', 'Tablesof8', 'Tablesof4to8']

# Dependent variable
y = benihana['Profit']

# Ensure that the "4shareatable" is included as a category for batching variables
for category in categorical_variables:
    if 'Batching' in category:
        benihana[category] = pd.Categorical(benihana[category], categories=batching_categories)

# One-hot encode categorical variables
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
