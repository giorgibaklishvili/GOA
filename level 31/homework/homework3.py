def password(correct_password):
    while True:
        password = input("Eneter your password: ")
        if password == correct_password:
            print("password is correct")
            break
        else:
            print("password is incorrect, try again")

correct_password = "1234"
password(correct_password)