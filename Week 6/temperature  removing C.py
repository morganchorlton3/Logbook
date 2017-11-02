
celsius = str(input ('Enter a temperature in celsius: '))

celsius = celsius.replace(' ', '')[:-1].upper()
celsius = float(celsius)

fahrenheit = float(celsius * 1.8) + 32

print(celsius ,'C is equal to' , fahrenheit , 'F')