from random import choice
from string import ascii_lowercase

print('Hi, to access the secret message please enter the password: ')

def input_password():
    global password_generation
    password_generation = (''.join(choice(ascii_lowercase) for i in range(12)))
    global password
    password = str(input('> '))

def check_password():
    while 1:
        if password_generation == password:
            print('Correct you now have access to the secret message')
            print('\n The secret message is \" The Eggs are cracked \"')
            break
        else:
            print('Incorrect password please try again!')
            input_password()
input_password()
check_password()
