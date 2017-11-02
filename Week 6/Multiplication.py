# Multiplication
__author__ = "Morgan Chorlton"
__email__ = "morgan.chorlton3@gmail.com"

from random import randint

attempts = 0

for c in range(0,5):
    first_digit = randint(0,11)
    second_digit = randint(0,11)
    while True:
        result = int(input(str(first_digit) + 'X' + str(second_digit) + '='))
        if first_digit * second_digit == result:
            print('Correct')
            attempts += 1
            break
        else:
            print('Incorrect, Please try again')
            attempts += 1

print('Your​ ​average​ ​attempts​ ​per​ ​problem​ ​was:​ ' ,attempts/5 )