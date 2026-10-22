try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print ("invalid value")

try:
    age= int(input("age: "))
    income = 20000
    risk = income/age
    print (age)
except ZeroDivisionError:
    print ("You cannot divide by zero")
except ValueError:
    print ("invalid value")

secret_number = 25
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess =int(input ("Guess : "))
    guess_count += 1
    if guess == secret_number:
        print ("you won! ")
        break

else:
    print ("you lost! ")
