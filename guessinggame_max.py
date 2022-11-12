print('Hey!')
print('do you want to play a game?')
choice=input('Y/N:')
choice=choice.lower()
counter=0
while choice not in['y','n']:
    choice=input('What?:')
    choice=choice.lower()
if choice == 'y':
    print('i\'ll think of a number and we\'ll see how long it takes for you to guess it')
    import random
    rannumber=random.randint(1,100)
while choice=='y':
    counter+=1
    guess=int(input('guess:')) 
    if guess==rannumber:
        if counter ==1:
            print('go buy a lottery ticket!!!')
            print('you got it on your first shot!!!')
        elif counter>1:
            print('Thats it! and it only took',counter,'Guesses')
        choice=rannumber
    elif guess<rannumber:
        print('\tTo low... ')
    elif guess>rannumber:
        print('\tTo high... ')
if choice == ('n'):
        print('oh... ok, goodbye')
    
