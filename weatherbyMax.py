print('Welcome to the Weather Analyzer!!')
print()
units = str(input('Enter "f" for Fahrenheit or "c" for Celsius:'))

units = units.lower()

while units not in['f','c']:
    print('Invalid Units!')
    print('Try again')
    units = str(input('Enter "f" for Fahrenheit or "c" for Celsius:'))

temp=int(input('Enter Temperature:'))
if units=='c':
    temp=temp*9/5+32
print(temp,'Degrees Fahrenheit')
if temp>=80:
    print ('It\'s pretty hot out!')
elif temp<60:
    print('It\'s kinda chilly!')
else:
    print('Perfect day for a walk!')

