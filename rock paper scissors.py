
import random

emojis = {'r' : '🪨', 'p' : '📃', 's' : '✂️'}
choices = ('r', 'p', 's')


while True:
   user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
   match True:
       case _ if user_choice not in choices:
           print("Invalid input")
           continue

   computer_choice = random.choice(choices)
   match computer_choice:
       case _:
           print(f"you chose {emojis[user_choice]}")
           print(f"computer chose {emojis[computer_choice]}")

   match (user_choice, computer_choice):
       case _ if user_choice == computer_choice:
           print("it's a tie")

       case _ if (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
           print("You win")

       case _:
           print("you lose")

   should_continue = input("Do you want to play again? (y/n): ").lower()
   match should_continue:
       case "n":
           break









