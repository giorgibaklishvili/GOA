weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))


bmi = weight / (height * height)


if bmi < 18.5:
    category = "Underweight"
elif bmi >= 18.5 and bmi <= 24.9:
    category = "Normal weight"
elif bmi >= 25 and bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"


print("Your BMI is: ", bmi)
print("You are categorized as: ", category)