import numpy as np
import itertools

# Coefficients from the regression
coef = {
    'Intercept': -406.15156055028496,
    'advertise': -165.07366673696703,
    'B_size': 0.03409680443188852,
    'Dining_1': -9.78201806884135,
    'Dining_2': -9.172864079740208,
    'Dining_3': 0.5662834754593359,
    'Opening': 5.100647918877722,
    'Campaign_HappyHour': 202.27043744126092,
    'Batching_1_SemBatch': -28.842276592865666,
    'Batching_1_Tablesof4to8': -26.24163743838283,
    'Batching_1_Tablesof8': 141.96740356490483,
    'Batching_2_SemBatch': -135.8014282765398,
    'Batching_2_Tablesof4to8': 67.20001044595135,
    'Batching_2_Tablesof8': 143.75577535765174,
    'Batching_3_SemBatch': -149.79866348163785,
    'Batching_3_Tablesof4to8': 58.898090316792626,
    'Batching_3_Tablesof8': 53.272564791746674,
}

# Define ranges for variables
dining_range = range(45, 76)  # Simplified range for Dining_x variables
opening_values = [210, 270, 330]
batching_values = ['SemBatch', 'Tablesof4to8', 'Tablesof8']
campaign_types = ['Awareness', 'HappyHour']  # Assume binary choice for simplicity

# Generate all combinations (simplified for this example)
combinations = list(itertools.product(dining_range, dining_range, dining_range, opening_values, batching_values, batching_values, batching_values, campaign_types))

# Function to calculate profit based on a combination of variables
def calculate_profit(combination):
    Dining_1, Dining_2, Dining_3, Opening, Batching_1, Batching_2, Batching_3, Campaign = combination
    # Simplify: Assume B_size and advertise are constant in this calculation for demonstration
    B_size = 50  # Placeholder value
    advertise = 1  # Placeholder value
    
    # Calculate profit using the regression coefficients
    profit = coef['Intercept'] + coef['advertise'] * advertise + coef['B_size'] * B_size + \
             coef['Dining_1'] * Dining_1 + coef['Dining_2'] * Dining_2 + coef['Dining_3'] * Dining_3 + \
             coef['Opening'] * Opening + \
             (coef['Campaign_HappyHour'] if Campaign == 'HappyHour' else 0)  # Simplified handling of Campaign
    
    # Add batching effect
    for Batching in [Batching_1, Batching_2, Batching_3]:
        if Batching == 'SemBatch':
            profit += coef['Batching_1_SemBatch']  # Simplification for demonstration
        elif Batching == 'Tablesof4to8':
            profit += coef['Batching_1_Tablesof4to8']  # Simplification for demonstration
        elif Batching == 'Tablesof8':
            profit += coef['Batching_1_Tablesof8']  # Simplification for demonstration
    
    return profit

# Find the combination with the highest profit
max_profit = -np.inf
best_combination = None
for combination in combinations:
    profit = calculate_profit(combination)
    if profit > max_profit:
        max_profit = profit
        best_combination = combination

print(f"Best combination for maximum profit: {best_combination}, with an estimated profit of {max_profit}")
