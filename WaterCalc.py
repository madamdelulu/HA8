# Daily Water Intake Calculator
# Author: Anita

print("=== DAILY WATER INTAKE CALCULATOR ===")

# User input
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

# Base water need formula (ml)
# Roughly: 35 ml per kg of body weight for adults
# Adjust for age: less for older adults, slightly more for teenagers
if age < 18:
    water_ml = weight * 40
elif 18 <= age <= 55:
    water_ml = weight * 35
else:
    water_ml = weight * 30

# Adjust slightly for height
if height > 180:
    water_ml += 250
elif height < 160:
    water_ml -= 200

# Convert to liters
water_liters = water_ml / 1000

# Output result
print(f"\nRecommended daily water intake: {water_liters:.2f} liters")

# Health note
if water_liters < 2:
    print("You should drink at least 2 liters daily for good hydration.")
elif 2 <= water_liters <= 3.5:
    print("Perfect range! Keep it up")
else:
    print("That's quite a lot! Make sure to balance with electrolytes.")

print("\nCalculation completed successfully.")