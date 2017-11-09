# useless technical support help line
__author__ = 'Morgan Chorlton'
__email__ = 'morgan.chorlton3@gmail.com'
__date__ = '09/11/2017'

import random
from random import randint

answers = ['yes', 'no', 'maybe']
print('Hello user welcome to the technical support help line.')

def ask():
    global question
    print('Please enter you question.')
    question = input(str('> '))
    chance = randint(0,100)
    if chance > 10:
        exit()
    else:
        pass


def check():
    if 'windows' in str.lower(question):
        print('Try to reboot your PC')
    elif 'apple' in str.lower(question):
        print('this call will cost you £100 per minute')
    elif 'phone' in str.lower(question):
        print('Do a factory reset')
    else:
        print(random.choice(answers))
    repeat_question()

def repeat_question():
    global question
    print('Do you have another question for me, if you want to exit the application then type exit')
    question = input(str('>'))
    chance = randint(0, 100)
    if chance > 10:
        exit()
    else:
        pass
    if 'exit' in str.lower(question):
        exit()
    else:
        check()

ask()
check()