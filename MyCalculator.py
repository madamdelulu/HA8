# BMI Calculator with Age
# Author: Anita

print("=== BMI CALCULATOR WITH AGE ===")

# user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))
if weight < 0:
    print('Weight cannot be negative. Must've been a misteak: switched to a positive number')
    weight = abs(weight)
height = float(input("Enter your height in meters: "))
if height < 0:
    print('Height cannot be negative. Must've been a misteak: switched to a positive number')
    height = abs(weight)

# BMI formula: weight / height^2
bmi = weight / (height ** 2)

print(f"\n{name}, your BMI is: {bmi:.2f}")

# classify BMI
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 25:
    category = "normal weight"
elif 25 <= bmi < 30:
    category = "overweight"
else:
    category = "obese"

# print general result
print(f"You are classified as: {category}")

# add age-based comments
if age < 18:
    print("Note: BMI interpretation for minors may differ. Consult a doctor for accurate assessment.")
elif age > 65:
    print("For older adults, BMI may not fully reflect body composition. Focus on healthy habits.")
else:
    print("Keep a balanced diet and stay active!")

print("\nCalculation completed successfully.")
