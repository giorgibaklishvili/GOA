age = int(input("Enter your age: "))
driving_experience = int(input("Enter your driving experience in years: "))

if age >= 18 and driving_experience >= 1:
    print("You are eligible to get a driver's license.")
else:
    print("You are not yet eligible to get a driver's license.")