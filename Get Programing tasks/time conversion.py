minutes_to_convert = int(input ('Hi, user please can you enter you minutes you would like to convert:'))

hours_decimal = minutes_to_convert/60
hours_part = int(hours_decimal)

minutes_decimal = hours_decimal-hours_part
minutes_part = round(minutes_decimal*60)

print('Hours:' , hours_part)
print('minutes: ' , minutes_part)
