import pandas as pd
import statsmodels.api as sm

# Load the dataset
data = pd.read_csv('Benihana3.csv')

# If necessary, convert 'Campaign', 'Batching_1', 'Batching_2', 'Batching_3' into dummy variables
data = pd.get_dummies(data, columns=['Campaign', 'Batching_1', 'Batching_2', 'Batching_3'], drop_first=True)

# Assuming 'Profit' is your target variable
X = data.drop('Profit', axis=1)  # Include all other variables as predictors
y = data['Profit']  # Profit as the response variable

# Adding a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print out the summary statistics of the model
print(model.summary())
