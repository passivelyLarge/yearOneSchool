print('\t"Old Macdonalod"')
print()
def refrain():
    print('Old MacDonald had a farm\nEe i ee i o')  
def verse(animals,sound):
    refrain()
    print('And on his farm he had some',animals,'\nEe i ee i o')
    print('With a',sound,sound,'here\nAnd a', sound,sound, 'there')
    print('Here a ', sound,', there a ', sound, sep='')
    print('Everywhere a ',sound,sound)
    refrain()
def main():
    animals='cows'
    sound='moo'
    verse(animals,sound)
    print()
    animals='chicks'
    sound='cluck'
    verse(animals,sound)
    print()
    animals='ducks'
    sound='quack'
    verse(animals,sound)
main()