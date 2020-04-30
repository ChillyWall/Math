number = 7
guese = int(input('''Now let's play a game. Guese what number I am thinking. Type here:'''))

if guese == number:
    print('Congratulations, you guessed it.')
    print('(but you do not win a prizes!)')
elif guess < number:
    print('No, it is a little higher than than that')
else :
    print('No, it is a little lower than that')

print('done')
