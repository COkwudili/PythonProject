correct_pin = "1234"

balance = 50000
attempts = 0
authenticated = False

print ("WELCOME TO OPAY WORLD")
while attempts < 3:
    entered_pin = input("enter your pin: ")

    match entered_pin == correct_pin:
        case True:
            print("pin correct")
            authenticated = True
            break

        case False:
            attempts += 1
            print("incorrect pin")
            print("attemmpts remaining:", 3-attempts)

match authenticated:
    case True:
        running = True

        while running:
            print("ATM MENU")
            print("1. check balance")
            print("2. deposit money")
            print("3. withdraw money")
            print("4. exit")

            choice = input("enter your choice: ")
            match choice:
                case "1":
                    print(f"available balances: {balance: .2f}")

                case "2":
                    amount = int(input("enter amount to deposit: "))

                    match amount > 0:
                        case True:
                            balance +=amount
                            print ("deposit successful")
                            print(f"new balance: {balance: .2f}")

                        case False:
                            print("invalid deposit amount. ")

                case "3":
                    amount = int(input("enter amount to withdraw: "))
                    match (amount <= 0, amount > balance):
                        case (True, _):
                            print ("invalid withdrawal amount. ")

                        case (False, True):
                            print ("insufficient funds. ")

                        case (False, False):
                            balance -= amount
                            print ("please collect your cash")
                            print(f"new balance: {balance: .2f}")

                case "4":
                    print ("THANK FOR USING OPAY WORLD")
                    running = False

                case _:
                    print ("invalid choice. select 1-5. ")

    case False:
        print("invalid choice. select 1-5. ")




