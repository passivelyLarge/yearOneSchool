print('Welcome to Average MPG calculator!')
line=('<>'*64)
print(line)
so=int(input('Please enter the miles on the odometer before the trip started:'))                        #so = starting odometer
print()
oo=int(input('Please enter the miles on the odometer after the first leg of the trip:'))                #oo = ongoing odometer
print()
counter=0
old=oo                                                 #old= hold the old odometer reading so i can subract it from the new one so i can get each legs miles
gastotal=0                                             #gastotal= so i can compute average later (just need to define it early)                                                
while so>=oo :                                                                                           
    print()
    print('invalid odometer readings! please double check!')
    print()
    so=int(input('Please enter the Miles on the odometer before the trip started:'))    
    print()
    oo=int(input('Please enter the Miles on the odometer after the first leg of the trip:')) 
    print()
gas=int(input('Please enter the Galons of fuel used on the first leg of your trip:')) 
print()
gastotal+=gas
mpg=round((oo-so)/gas,2)
counter+=1
print(mpg,'MPG \nfor that leg')                 
print()
yn=input('did you have another leg on your trip?   (Y/N):').lower()                                      #yn = yes/no variable
while yn!=('y') and yn!=('n'):
    print()
    yn=input('Please enter "y" or "n":')
while yn==('y'):
    print()
    oo=int(input('Please enter the odometer reading after that leg:'))
    print()
    while old>=oo :
        print('invalid odometer readings! please double check!')
        print()
        oo=int(input('Please enter the odometer reading after that leg:'))
        print()
    gas=int(input('please enter the amount of gas used on that leg:'))                                                                                              
    print()
    gastotal+=gas
    mpg=round((oo-old)/gas,2)                                                                            
    counter+=1
    old=oo
    print(mpg,'MPG')
    print('for leg number',counter)
    print()
    yn=input('did you have another leg on your trip?   (Y/N):').lower()
    while yn!=('y') and yn!=('n'):
        print()
        yn=input('Please enter "y" or "n":')
if yn==('n'):
    mpg=round((oo-so)/gastotal,2)
    print()
    print(mpg,'MPG, was your average over',counter,'legs')
    print()
    print('Goodbye')
    print(line)                                                 #ended up adding a lot of print() so it was easier to follow when testing
                                                                #but they really arent needed... please let me know if i should remove them for a better grade
                                                                #or if you want me to seperate the legs with other characters or something


