def temperature():
    print('select the what temperature you would like to calculate:')
    print('1 = Celsius to fahrenheit')
    print('2 = fahrenheit to celsius')
    decision = int(input())

    if decision == 1:
        celsius = float(input ('Enter a temperature in celsius: '))

        fahrenheit = float(celsius * 1.8) + 32
        print(celsius ,'C is equal to' , fahrenheit , 'F')
    elif decision == 2:
        fahrenhiet2 = float(input('Enter a temperature in fahrenheit: '))

        celsius2 =  float(fahrenhiet2 - 32) * 0.5556
        print (fahrenhiet2 , 'F is equal to' , celsius2 , 'C')
    else:
        print('Invalid choice, please re run the program.')

    temp_again = input('''
Do you want to convert another temperature?
Please type Y for YES or N for NO.
''')

    if temp_again.upper() == 'Y':
        temperature()
    elif temp_again.upper() == 'N':
        print('See you later.')


temperature()