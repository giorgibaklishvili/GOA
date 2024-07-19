gpa = float(input("Enter your GPA (Grade Point Average): "))
income = float(input("Enter your income: "))

if gpa >= 3.5:
    print("Congratulations! You get the scholarship.")
    print("Scholarship amount: $1000")
elif gpa >= 3.0 and income < 50000:
    print("Congratulations! You get the top scholarship.")
    print("Scholarship amount: $2000")
else:
    print("Sorry, you cant use any scholarship at this time.")