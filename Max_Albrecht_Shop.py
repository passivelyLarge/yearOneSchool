#  Max Albrecht's Coffee shop, Sep 30 2022

print ('Welcome to Pikachu Coffee')
line='^-'*30
print (line)
print ('\tPikachu!\n\t (\\__/)\n\t (o^.^)\n\tZ(\'(")")')
print (line)
day=int(input('Enter the Day of the Month:'))
while day>31:
    print('Invalid Day!')
    print('Please try again.')
    day=int(input('Enter the Day of the Month:'))
else:
    lb=int(input('How many Pounds of Coffee do you want?:'))
    while lb>50:
        print('too Much Coffee!')
        print('Please enter an amount under 50LBs')
        lb=int(input('How many Pounds of Coffee do you want?:'))
    else:
        print(line)
        cost=lb*8.50
        ship=round(5.55+lb*.65,2)
        tax=round(round((31-day)/5,2)*cost/100,2)
        total=round(cost+ship+tax,2)
        print("Cost","\tShipping","Tax%","\tTotal",sep="\t")
        line1='--'*26
        print(line1+'--------')
        print(cost,ship,tax,total,sep="\t\t",end='\n'+'Tomorrow'+line1+'\n')
        day+=1
        if day > 31:
            day-=31
        tax=round(round((31-day)/5,2)*cost/100,2)
        total=round(cost+ship+tax,2)
        print(cost,ship,tax,total,sep="\t\t",end='\n'+'Next Day'+line1+'\n')
        day+=1
        if day > 31:
            day-=31
        tax=round(round((31-day)/5,2)*cost/100,2)
        total=round(cost+ship+tax,2)
        print(cost,ship,tax,total,sep="\t\t",end='\n'+line1+'--------'+'\n')

print('Pika Pika!')

