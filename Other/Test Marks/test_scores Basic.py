name = input('Enter the student\'s name: ')

mark_1 = int (input('Enter first result: '))
mark_2 = int (input('Enter first result: '))
mark_3 = int (input('Enter first result: '))
mark_4 = int (input('Enter first result: '))
mark_5 = int (input('Enter first result: '))

total_marks = mark_1 + mark_2 + mark_3 + mark_4 + mark_5

average_marks = total_marks / 5

print()
print('The final mark for ' + name + 'is' + str(average_marks))

if average_marks >= 70.0:
    print('Awesome', )