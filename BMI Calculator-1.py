weight = int(input())  # in kilograms
height_cm = int(input())  # in centimeters

# Convert height to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m * height_m)

# Round BMI to 1 decimal place
bmi_rounded = round(bmi, 1)

# Print BMI
print(bmi_rounded)

# Determine and print BMI category
if bmi_rounded < 18.5:
    print("Underweight")
elif 18.5 <= bmi_rounded <= 24.9:
    print("Normal weight")
elif 25 <= bmi_rounded <= 29.9:
    print("Overweight")
else:
    print("Obese")
