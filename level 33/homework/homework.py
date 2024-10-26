def simple_calculator(num1,num2,operation):
    if operation == "-":
        return num1 - num2
    elif operation == "+":
        return num1 + num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif num1 == 0 or num2 == 0:
        return 'you cant devide by 0'
    

num1 = int(input("Enter First num: "))
operation = input("Enter an operation '+,-,*,/': ")
num2 = int(input("Enter Second num: "))
print(simple_calculator(num1,num2,operation))