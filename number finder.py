import time
import random
F = 0

number = int(input('What number do you want me to find? '))
if number <= 1000000 and number > 0:
    print('Okay, searching now')
    time.sleep(.4)
    print('Initiating hacks')
    time.sleep(.4)
    print('Database found')
    time.sleep(.4)
    print('Attempting login')
    time.sleep(.4)
    print('Login successful')
    time.sleep(.4)
    print('Searching for number')


    while F!= number:
        F = random.randint(0,1000000)
    if F == number:
        print(number)
        print('Great, I hacked into the database')
        for i in range(0,1):
            print('Hack success!')


elif True:
    print('Oh no, number too chunky!')



