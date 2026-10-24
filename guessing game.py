import random

number_to_guess = random.randint(1,10)
while True:
    try:

        guess = int(input("Guess a number between 1 and 100: "))

        match True:
            case _ if guess < number_to_guess:
                print("Too low")

            case _ if guess > number_to_guess:
                print("Too high")

            case _:
                print("congratulations! you guessed the number")
                break


    except ValueError:
        print("Please enter a valid number")


