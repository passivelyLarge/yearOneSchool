print('Welcome to the Trip time calculator')
print('\t|\n\tV')
miles=float(input('enter number of miles to be traveled:'))
speed=float(input('enter miles per hour:'))
print('\t|\n\tV')
print(int(miles/speed),('\tHours'))
decimal=(miles/speed)%1
print(int(decimal*60),('\tMinutes'))
