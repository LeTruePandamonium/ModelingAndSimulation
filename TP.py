import numpy as np
import matplotlib.pyplot as plt

def calorie_burn_per_min(weight, speed):
    """Calculate calories burned per minute while walking."""
    return (0.035 * weight) + ((speed**2 / 1.75) * 0.029 * weight)

def fat_loss_simulation(initial_weight, speed_kmh, walking_minutes, daily_calories, basal_calories, days):
    """Simulate weight loss over a given number of days."""
    speed_mps = speed_kmh / 3.6  # Convert km/h to m/s
    calories_per_min = calorie_burn_per_min(initial_weight, speed_mps)
    calorie_per_kg_fat = 7700  # 1 kg of fat = 7700 kcal
    
    weights = [initial_weight]
    for _ in range(days):
        calories_burned = calories_per_min * walking_minutes
        daily_deficit = (basal_calories + calories_burned) - daily_calories
        fat_loss = daily_deficit / calorie_per_kg_fat
        new_weight = weights[-1] - fat_loss
        weights.append(new_weight)
    
    return weights

# Simulation parameters
initial_weight = 95  # kg
speed_kmh = 5  # km/h (moderate walking speed)
walking_minutes = 90  # Walking duration per day
basal_calories = 2000  # BMR (estimated daily energy expenditure without activity)
daily_calories = 1800  # Fixed daily calorie intake
days = 365  # One year simulation

# Run simulation
weights = fat_loss_simulation(initial_weight, speed_kmh, walking_minutes, daily_calories, basal_calories, days)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(range(days + 1), weights, marker='o', linestyle='-')
plt.xlabel('Days')
plt.ylabel('Weight (kg)')
plt.title('Fat Loss Simulation Over One Year')
plt.grid()
plt.show()
