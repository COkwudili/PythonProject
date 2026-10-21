correct_pin = "1234"
balance = 50000
attempts = 0
authenticated = False

print ("Welcome to the Atm")
while attempts < 3:
    entered_pin = input("enter your pin: ")

    match entered_pin == correct_pin:
        case True:
            print("Pin is correct,welcome")
            authenticated = True

        case False:
            attempts += 1
            print("incorrect pin")
            print()

