name = (input('Enter the students name: '))
Number_of_results = int(input('Enter the number of result: '))

results = []
for count in range(Number_of_results):
    while 1:
        result = int(input ('Enter result #' + str(count +1) + ': '))
        if result in range (0,101):
            results.append (result)
            break
        else:
            print('Invalid. Try agian.')
print('\n Average is: ', sum (results) / len(results))
