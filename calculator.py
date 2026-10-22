
print("WELCOME TO THIS CALCULATOR")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exit")

choice = input("choose a number(1-5): ")
match choice:
    case "1":
        number1 = int(input("enter your first number: "))
        number2 = int(input("enter your second number: "))
        print ("RESULT:", number1 + number2)

    case "2":
        number1 = int(input("enter your first number: "))
        number2 = int(input("enter your second number: "))
        print ("RESULT:", number1 - number2)

    case "3":
        number1 = int(input("enter your first number: "))
        number2 = int(input("enter your second number: "))
        print ("RESULT:", number1 * number2)

    case "4":
        number1 = int(input("enter your first number: "))
        number2 = int(input("enter your second number: "))
        print ("RESULT:", number1 / number2)

    case "5":
        print("THANKS FOR USING THIS CALCULATOR")

    case _:
        print("INVALID INPUT")