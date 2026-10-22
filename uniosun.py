result = 4.00
password = "12345"
authenticated = False
print("WELCOME TO UNIOSUN PORTAL")
course_reg = 'physics, chemistry, biology'

while True:
    entered_password = input("Enter your password: ")

    match entered_password == password:
        case True:
            print("PASSWORD CORRECT")
            authenticated = True
            break

        case False:
            print("INCORRECT PASSWORD")
            print("TRY AGAIN")

match authenticated:
    case True:
        running = True

        while running:
            print("1. CHECK RESULT")
            print("2. PRINT RESULT OUT")
            print("3. REGISTER COURSES FOR EXAM")
            print("4. PRINT COURSE REGISTRATION FORM")
            print("5. EXIT")

            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    print(f"RESULT: {result: .2f}")

                case "2":
                    print("RESULT PRINTED OUT")

                case "3":
                    registration = input("Enter your course registration: ")
                    match registration == course_reg:
                        case True:
                            print("COURSE REGISTRATION SUCCESSFUL")


                        case False:
                            print("INCORRECT REGISTRATION")

                case "4":
                    print("COURSE REGISTRATION SLIP PRINTED SUCCESSFULLY")

                case "5":
                    print("HAVE A NICE DAY! ")
                    running = False

                case "_":
                    print("INVALID ENTRY")








