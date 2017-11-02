from random import choice
from string import digits
import time

print('Hi, please enter a code (using 0,1,2,3,4,5,6,7,8,9) and I will try to guess it  ')
password = str(input('> '))
def check():
    count = 0
    if password_generation != password:
        print(password_generation, 'Incorrect, trying again ...')
        while password_generation == password:
            count += 1
            break
        password_gen()
    else:
        print('Got it your combination is ', password_generation)
        print('It took' ,count ,'try\'s to get your combination')
        exit

def password_gen():
    global password_generation
    password_generation = (''.join(choice(digits) for i in range(len(password))))
    time.sleep(0.2)
    check()
password_gen()

