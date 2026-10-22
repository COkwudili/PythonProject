admission_status = "you have been admitted"
password = "thank god"
enter_password = input("enter your password: ")
if enter_password == password:
    while True:
        print("YOU ARE LOGGED IN")
        print("1. check admission status")
        print("2. pay acceptance fee")
        print("3. pay medical fee")

        print("4. EXIT")

        choice = input("Enter your choice: ")
        if choice == "1":
            print(f'your admission status is {admission_status}')

        elif choice == "2":
            acceptance_fee = int(input("enter your acceptance fee: "))
            if acceptance_fee == 15000:
                print("PAYMENT SUCCESSFUL")
            else:
                print ("payment must be 15000 only")

        elif choice == "3":
            medical_fee = int(input("enter your medical fee: "))
            if medical_fee == 15000:
                print("PAYMENT SUCCESSFUL")
            else:
                print("medical fee must be 15000 only")

        elif choice == "4":
            print("EXIT")
            break

else:
    print("wrong password")
