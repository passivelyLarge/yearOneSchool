print('Welcome to the Trip time calculator')
print('\t|\n\tV')
miles=float(input('enter number of miles to be traveled:'))
speed=float(input('enter miles per hour:'))
print('\t|\n\tV')
print('\t',int(miles/speed),('\tHours'))
decimal=(miles/speed)%1
print('\t',int(decimal*60),('\tMinutes'))
