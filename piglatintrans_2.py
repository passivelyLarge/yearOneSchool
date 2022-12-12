def welcome():
        print('Welcome to pig latin translator!\n')
def puncRemove(sentence):
    punc= ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+',']','[','}','{',';',':','"',"'",',','<','>','.','?','/'] 
##    for x in range(len(sentence)):
##        sentence=str(sentence)
##        sepSent=sentence.split(punc)      #was trying something but it didnt work, but i kept it in as a reminder that it wont work... cant split with list
##        
##    return newSentence
    ##sentence=sentence      #i think i was just really tired.... commented it out cause it gave me a laugh going back over my code before submitting it
    for x in sentence:
            if x in punc:
                    sentence=sentence.replace(x,' ')
                    #print(sentence)                    debug
            elif x not in punc:
                    pass
                    #print(sentence)                    debug
                    
    return sentence

        
def trans():
        lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']   #looked up the rules to pig laten and these are what they said was considered the first letter as well
        sentence = str(input('What sentence would you like to convert into Piglatin: '))
                         
                
        sentence = puncRemove(sentence)           #tried to get rid of punc here without making its own function but it was a hassle so i made it elswhere
        sentence = sentence.split()
        for w in range(len(sentence)):
                a = sentence[w]

                if a[0] in ['a', 'e', 'a', 'o', 'u']:
                        sentence[w] = a +'ay'
                elif translated(a) in lst:
                        sentence[w] = a[2:]+a[:2]+'ay'              #getting this right was a pain
                elif a.isalpha() == False:
                        sentence[w] = a
                else:
                        sentence[w] = a[1:]+a[0]+'ay'
        return ' '.join(sentence)
def translated(str):
        return str[0]+str[1]

def main():
    welcome()
    again='y'   
    while again=='y':
        output=trans()
        print('\ntranslation =>',output,'\n')
        again=input('another sentence? y/n:').lower()     #i think im going to create an again file one of these days just to import or copy an paste so i dont have to make it everytime
        print()
        while again != 'y' and again != 'n':
            print('\nnot a valid input\n')
            again=input('another sentence? y/n:').lower()
            print()
        if again == 'n':
            print('Goodbye!')
            quit
       
if __name__ == "__main__":
    main()