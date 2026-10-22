import random

choice_1 = "y"
choice_2 = "n"

while True:
    choice = input("Roll the dice? (y/n): ")
    match choice:
        case "y":
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(f"({die1}, {die2})")

        case "n":
            print("Good bye! ")
            break

        case "_":
            print("invalid entry")


