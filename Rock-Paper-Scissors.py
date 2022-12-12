import random
def battle(player : str , computer):
    player=player.upper()
    if player == computer:
        point = 0
    elif player == ('R') and computer == ('S'):
        point = 1
    elif player == ('S') and computer == ('P'):
        point = 1
    elif player == ('P') and computer == ('R'):
        point = 1
    else:
        point = 2
    return point


def hand(finger):                             #trying out a dictionary, https://www.geeksforgeeks.org/switch-case-in-python-replacement/
    fingers = {
        0: 'R',
        1: 'P',
        2: 'S',
    }
    return fingers.get(finger)


def welcome():
    print('Welcome to Rock, Paper, Scissors!\nhere are the rules:')
    print('Scissors wins over Paper, but loses to Rock, Paper wins over Rock, but loses to Scissors, Rock wins over Scissors, but loses to Paper')
    print()

def main():
    welcome() 
    again=input('Ready? y/n:').lower()
    print()
    counter=0
    p_score=0
    c_score=0
    while again != 'y' and again != 'n':
        print('\nnot a valid input\n')
        again=input('ready? y/n:').lower()

    again = rockPaperScissors(again, counter, p_score, c_score)
        
    if again == 'n':
        print('Goodbye!')
        quit

def rockPaperScissors(again, counter, p_score, c_score):
   
    while again == 'y':
        ran=random.randint(0,2)
        computer=hand(ran)
        player=input('Please enter "R","P", or "S":')
        print()
        while player not in ('r','p','s','R','S','P'):
            player=input('Invalid! try again:')
        point=battle(player,computer)
        if point==1:
            p_score+=1
            counter+=1
            print('you won that round')
            scoreTotal(counter, p_score, c_score)
            print()
        elif point==2:
            c_score+=1
            counter+=1
            print('I won that round')
            print()
            scoreTotal(counter, p_score, c_score)
            print()
        elif point==0:
            counter+=1
            print('tie!!!')
            scoreTotal(counter, p_score, c_score)
        
        again=input('Again? y/n:').lower()
        print()
    return again

        
def scoreTotal(counter, player_score, computer_score):
    print('the score is',player_score,'to',computer_score,'at the end of round',counter)
    
    
          
main()