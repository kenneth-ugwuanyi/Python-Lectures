def login():
    trial = 0
    while True:
        user_name = input("Please enter your User Name: ")
        password = input("Please enter your Password: ")
        trial += 1
        if trial > 2:
            print(f"security violation! you have exceeded {trial} trials allowed, please contact the system admin")
        elif user_name == "Kenneth" and password == "Enter":
            print("Welcome to UBA Payroll system")
            break
        else:
            print(f"invalid log in details, you have {3 -trial} trial left ")
login()

