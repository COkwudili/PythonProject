 print ('chinedu okwudili')
print ('o----')
print (' ||||')
print ('*' * 10)
price = 20
name = 'john'
cage = 20
is_new = True
print (price)
print (name + ' is ' + str(cage) + ' new_patient')
name = input ('what is your name? ')
print ('hi ' + name)
name = input ('what is your name? ')
favorite_color = input ('what is your favorite color? ')
print (name + ' likes ' + favorite_color)
birth_year = input ('what is your birth year? ')
print (type(birth_year))
age = 2026-int(birth_year)
print (type(age))
print (age)
weight_in_pounds = input ('weight_in_pounds: ')
weight_in_kilogram = int  (weight_in_pounds) * 0.45
print (weight_in_kilogram)
course = "pyhton's course for beginners"
print (course)
course = 'python for "beginners"'
print (course)
course = '''
hi john

here is our first email to you

thank you,
the support team
'''
print (course)
course = 'python for beginners'
print (course[1:])
course = ('python for beginners')
print (course[1:-1])
first_name = 'john'
last_name = 'smith'
message = f'{first_name} { last_name} is a coder'
print (message)
course = 'python for beginners'
print (course.replace('p', 'j'))
print (course.upper())
print(len(course))
print (10//3)
x = 10
x -= 3
print (x)
is_hot = True
is_cold = False

if is_hot:
    print ("it's a hot day")
    print ("drink plenty of water")

elif is_cold:
    print ("it's a cold day")
    print ("wear warm clothes")

else:
    print ("it' a lovely day")

print ("enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1

else:
    down_payment = price * 0.2

print (f"down_payment: ${down_payment}" )

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print ("eligible for loan")

temp = 30

if temp > 30:
    print ("it's a hot day")

else:
    print ("it's not a hot day")

name = ('j')
if len (name)<3:
    print ("name must be at least 3 characters")

elif len (name)>50:
    print ("name must be maximum of 50 characters")

else:
    print ("name looks good")

weight = int (input('weight: '))
unit = input ('(L) bs or (k)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print (f"you are {converted} kilos")

else:
    converted = weight / 0.45

    print (f"you are {converted}"
           f" pounds")

i = 1
while i <=5:
    print ('*' * i)
    i = i + 1
print ("done")

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int (input ('guess: '))
    guess_count += 1
    if guess == secret_number:


        print ("you won")
        break
else :
    print ('you lost! ')
    

command = ""
while True :
    command = input ("< ").lower()
    if command == "start" :
        print ("car started...")
    elif command == "stop" :
        print ("car stopped.")
    elif command == "help" :
        print('''
    start - to start the car
    stop - to stop the car
    quit - to quit
        ''')
    elif command == "quit" :

        break
    else :
        print ("sorry, i don't understand")

for item in ('python') :
    print (item)



for item in ['mosh', 'john', 'sarah'] :
    print (item)

for item in range (10) :
    print (item)
for item in range (5,10) :
    print (item)
for item in range (5,10,2) :
    print (item)

prices = [10, 20, 30]

total= 0
for price in prices :
    total += price
print(total)

numbers = [5, 2, 5, 2, 2]
for number in numbers :
    print ('x' * number)


numbers = [9, 5, 6, 7, 15, 4]
highest = numbers [0]
for number in numbers :
    if number > highest :
        highest = number

print (highest)

numbers = [3, 6,7, 8, 14]
lowest = numbers [0]
for number in numbers :
    if number < lowest :
        lowest = number
print (lowest)



























