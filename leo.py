secret_number = 11
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int (input ('guess: '))
    guess_count += 1
    if guess == secret_number:
        print ("you won! ")
        break
else:
    print ("you lost! ")


command= ""
started = False
while True:
    command = input ("<").lower()
    if command == "start":
        if started:
            print ("car already started")
        else:
            started = True
            print ("car started! ")
    elif command == "stop":
        if not started:
            print ("car already stopped")
        else:
            started = False
            print ("car stopped! ")
    elif command == "help":
        print ("""
start - starts the car
stop- stops the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:

        print ("sorry, i dont understand")

prices = [10, 20, 30]
total_price = 0
for price in prices:
    total_price += price
print (total_price)

for x in range (4):
    for y in range (3):
        print (f'({x},{y})')

numbers = (1,2,3,4,5,6,7,8,9)
for number in numbers:
    print ('x' * number)

numbers = (1,2,3,4,5,6,7,8,9)
highest = numbers[0]
for number in numbers:
    if number > highest:
        highest = number
print (highest)

numbers = [2,3,5,5,6]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print (unique)

phone_number = input("enter phone number: ")
digits_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
}
output = ""
for ch  in phone_number:
    output += digits_mapping.get(ch, "!") + " "
print (output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print (output)

def answer_user():
    print("you did a great job")
    print("nice.")


print ("start")
answer_user()
print ("stop")

class point:
    def __init__(self,x,y):

        self.x = x
        self.y = y


    def draw(self):
        print ("draw")


point= point(10,20)
print (point.x)









