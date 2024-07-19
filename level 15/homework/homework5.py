age = int(input("Enter your age: "))
if age <= 0:
    print("age is positive number")


purchase = float(input("Enter your total purchase amount"))
if purchase <= 0:
    print("amount should be positive number")


discount = False
discount_amount = 0.0

if age >= 60 and purchase >= 100:
    discount = True
    discount_amount = 0.15

elif age >= 60:
    discount = True
    discount_amount = 0.10

elif purchase >= 100:
    discount = True
    discount_amount = 0.05

if discount:
    print("discount_amount: ", discount_amount * 100, "%")

else:
    print("sorry you do not have any discount at this time")
    

