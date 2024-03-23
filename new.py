import numpy as np
import itertools

# Regression coefficients
coef = {
    'Intercept': -406.15156055028496,
    'advertise': -165.07366673696703,
    'B_size': 0.03409680443188852,
    'Dining_1': -9.78201806884135,
    'Dining_2': -9.172864079740208,
    'Dining_3': 0.5662834754593359,
    'Opening': 5.100647918877722,
    'Campaign_HappyHour': 202.27043744126092,
    # Assuming coefficients for batching as placeholders
    'Batching_1_SemBatch': 0,  # Placeholder
    'Batching_1_Tablesof4to8': 0,  # Placeholder
    'Batching_1_Tablesof8': 0,  # Placeholder
    'Batching_2_SemBatch': 0,  # Placeholder
    'Batching_2_Tablesof4to8': 0,  # Placeholder
    'Batching_2_Tablesof8': 0,  # Placeholder
    'Batching_3_SemBatch': 0,  # Placeholder
    'Batching_3_Tablesof4to8': 0,  # Placeholder
    'Batching_3_Tablesof8': 0,  # Placeholder
    # Placeholder values for batching effects, replace with actual coefficients
}

# Define ranges for variables based on provided constraints
b_size_range = range(15, 88, 8)  # From 15 to 87 in intervals of 8
dining_range = range(45, 76)  # From 45 to 75
advertise_range = np.arange(0, 4.1, 0.1)  # From 0 to 4 in 0.1 intervals
opening_values = [210, 270, 330]
campaign_types = ['Awareness', 'HappyHour']
batching_values = ['SemBatch', 'Tablesof4to8', 'Tablesof8']  # Assuming 3 options for simplification

# Function to calculate profit based on a combination of variables
def calculate_profit(advertise, b_size, dining_1, dining_2, dining_3, opening, campaign, batching_1, batching_2, batching_3):
    # Calculate profit using the regression coefficients
    profit = coef['Intercept'] + \
             coef['advertise'] * advertise + \
             coef['B_size'] * b_size + \
             coef['Dining_1'] * dining_1 + \
             coef['Dining_2'] * dining_2 + \
             coef['Dining_3'] * dining_3 + \
             coef['Opening'] * opening + \
             (coef['Campaign_HappyHour'] if campaign == 'HappyHour' else 0)

    # Placeholder for batching effects, assuming they're additive and not interacting
    profit += coef.get('Batching_1_' + batching_1, 0) + \
              coef.get('Batching_2_' + batching_2, 0) + \
              coef.get('Batching_3_' + batching_3, 0)
    return profit

# Start the search for the optimal combination
max_profit = -np.inf
optimal_combination = {}

for advertise, b_size, dining_1, dining_2, dining_3, opening, campaign, batching_1, batching_2, batching_3 in itertools.product(
    advertise_range, b_size_range, dining_range, dining_range, dining_range, opening_values, campaign_types, batching_values, batching_values, batching_values):
    profit = calculate_profit(advertise, b_size, dining_1, dining_2, dining_3, opening, campaign, batching_1, batching_2, batching_3)
    if profit > max_profit:
        max_profit = profit
        optimal_combination = {
            'advertise': advertise,
            'B_size': b_size,
            'Dining_1': dining_1,
            'Dining_2': dining_2,
            'Dining_3': dining_3,
            'Opening': opening,
            'Campaign': campaign,
            'Batching_1': batching_1,
            'Batching_2': batching_2,
            'Batching_3': batching_3
        }

print(f"Optimal combination for maximum profit: {optimal_combination}, with an estimated profit of {max_profit}")
