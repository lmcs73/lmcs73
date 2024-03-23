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
    'Batching_1_SemBatch': 0,  # Base category
    'Batching_1_4shareatable': 0,  # Adjust these coefficients based on your model
    'Batching_1_Tablesof8': 0,  # Adjust these coefficients based on your model
    'Batching_1_Tablesof4to8': 0,  # Adjust these coefficients based on your model
    'Batching_2_SemBatch': 0,  # Repeat for Batching_2
    'Batching_2_4shareatable': 0,
    'Batching_2_Tablesof8': 0,
    'Batching_2_Tablesof4to8': 0,
    'Batching_3_SemBatch': 0,  # Repeat for Batching_3
    'Batching_3_4shareatable': 0,
    'Batching_3_Tablesof8': 0,
    'Batching_3_Tablesof4to8': 0,
}

# Variable ranges
advertise_range = np.arange(0, 4.1, 0.1)
b_size_range = range(15, 88, 8)
dining_range = range(45, 76)
opening_values = [330, 270, 210]
campaign_types = ['Awareness', 'HappyHour']
batching_options = ['SemBatch', '4shareatable', 'Tablesof8', 'Tablesof4to8']

# Function to calculate profit for a given combination
def calculate_profit(advertise, b_size, dining_1, dining_2, dining_3, opening, campaign, batching_1, batching_2, batching_3):
    profit = coef['Intercept'] + \
             coef['advertise'] * advertise + \
             coef['B_size'] * b_size + \
             coef['Dining_1'] * dining_1 + \
             coef['Dining_2'] * dining_2 + \
             coef['Dining_3'] * dining_3 + \
             coef['Opening'] * opening + \
             (coef['Campaign_HappyHour'] if campaign == 'HappyHour' else 0) + \
             coef[f'Batching_1_{batching_1}'] + \
             coef[f'Batching_2_{batching_2}'] + \
             coef[f'Batching_3_{batching_3}']
    return profit

# Iterate over all combinations to find the one with the highest profit
max_profit = float('-inf')
best_combination = None

for combination in itertools.product(advertise_range, b_size_range, dining_range, dining_range, dining_range, opening_values, campaign_types, batching_options, batching_options, batching_options):
    current_profit = calculate_profit(*combination)
    if current_profit > max_profit:
        max_profit = current_profit
        best_combination = combination

print(f"Best combination for maximum profit: {best_combination}, with an estimated profit of {max_profit:.2f}")
