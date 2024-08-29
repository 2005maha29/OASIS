def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # Convert height from centimeters to meters
    bmi = weight_kg / (height_m ** 2)  # Calculate BMI
    return bmi

# Example usage
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")

# Optional: Display BMI category
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
