# useless technical support help line
__author__ = 'Morgan Chorlton'
__email__ = 'morganchorlton3@gmail.com'
__date__ = '09/11/2017'

from random import choice, randint, random
question =''
def chance():
    return random.random () > 0.9
while True :
    print('please enter you question, To exit type exit: ')
    question = input(str('>'))
    chance()
    if str.lower(question) == 'exit':
        exit()
    elif 'windows' in str.lower(question):
        print('Try to reboot your PC')
    elif 'apple' in str.lower(question):
        print('this call will cost you £100 per minute')
    elif 'phone' in str.lower(question):
        print('Do a factory reset')
    elif 'linux' in str.lower(question):
        print('Try to reboot you PC')
    elif 'help' in str.lower(question):
        print('Whats the problem?')
    else:
        print (choice(['yes', 'no', 'maybe']))