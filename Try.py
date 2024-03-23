import itertools
import numpy as np

# Coefficients from the regression model
coef = {
    'Intercept': -406.15156055028496,
    'advertise': -165.07366673696703,  # This will be adjusted based on campaign type below
    'B_size': 0.03409680443188852,
    'Dining_1': -9.78201806884135,
    'Dining_2': -9.172864079740208,
    'Dining_3': 0.5662834754593359,
    'Opening': 5.100647918877722,  # Adjusted below based on opening time
    'Campaign_HappyHour': 202.27043744126092,
    # Batching coefficients are for demonstration; assuming binary (0 or 1) for each
    'Batching_1_SemBatch': -28.842276592865666,
    'Batching_1_Tablesof4to8': -26.24163743838283,
    'Batching_1_Tablesof8': 141.96740356490483,
    'Batching_2_SemBatch': -135.8014282765398,
    'Batching_2_Tablesof4to8': 67.20001044595135,
    'Batching_2_Tablesof8': 143.75577535765174,
    'Batching_3_SemBatch': -149.79866348163785,
    'Batching_3_Tablesof4to8': 58.898090316792626,
    'Batching_3_Tablesof8': 53.272564791746674
}

# Variable constraints
opening_options = [330, 270, 210]
batching_options = ['SemBatch', 'Tablesof4to8', 'Tablesof8']
dining_range = [45, 75]

# Assume a simple approach to decide between Awareness and HappyHour based on profit impact
campaign_options = ['Awareness', 'HappyHour']

# For demonstration, we'll use fixed values for some variables and iterate over a few
best_profit = -np.inf
best_setup = None

# Iterate over a simplified and limited set of options
for opening in opening_options:
    for dining_1 in dining_range:
        for dining_2 in dining_range:
            for dining_3 in dining_range:
                for campaign in campaign_options:
                    # Calculate profit for this setup
                    # Simplified model: not considering advertise cost variation or detailed Batching_x calculations
                    profit = (coef['Intercept'] +
                              coef['B_size'] * 87 +  # Assuming a fixed B_size for simplification
                              coef['Dining_1'] * dining_1 +
                              coef['Dining_2'] * dining_2 +
                              coef['Dining_3'] * dining_3 +
                              coef['Opening'] * opening +
                              (coef['Campaign_HappyHour'] if campaign == 'HappyHour' else 0))
                    # Update best setup if this is the highest profit found
                    if profit > best_profit:
                        best_profit = profit
                        best_setup = (opening, dining_1, dining_2, dining_3, campaign)

print(f"Best Setup: {best_setup}, Profit: {best_profit}")
