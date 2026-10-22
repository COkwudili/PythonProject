balance = 50000
print ("WELCOME TO OPAY")
print ("1. check balance")
print ("2. deposit money")
print ("3. withdraw money")
print ("4. quit")

choice = input("Enter your choice: ")
match choice:
    case "1":
        print(f'your balance is {balance}')

    case "2":
        deposit_money = int(input("enter your deposit money: "))
        balance += deposit_money
        print("deposit successful")
        print(f'your new balance is {balance}')

    case "3":
        withdraw_money = int(input("enter your withdraw money: "))
        balance -= withdraw_money
        print("withdrawal successful")
        print(f'new balance: {balance}')

    case "4":
        print("THANK FOR USING OPAY")

    case _:
        print("please enter a valid choice")


