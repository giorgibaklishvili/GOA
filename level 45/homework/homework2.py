def check_number():
    number = float(input("გთხოვთ შეიყვანოთ რიცხვი: ")) 
    if number > 0:
        print("რიცხვი დადებითია.")
    elif number < 0:
        print("რიცხვი უარყოფითია.")
    else:
        print("რიცხვი ნულია.")

check_number()