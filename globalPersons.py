a = '>> '

def pamukTheCat(intelligence):
    print('You distracted by a cat laying on your way:')
    print(' - Pet It (>> 1)')
    print(' - Ask Its Name (>> 2)')
    print(' - Pass (>> P)')
    interaction = input(a)
    if (interaction == '1' and intelligence >= 1):
        print('You pet the cat')
    elif (interaction == '2' and intelligence >= 5):
        print('You asked for its name:')
        print(' - Its name is Pamuk The Cat')
    elif (interaction == 'P'):
        print('You past it without looking back')
    else:
        print('You are too dumb to communicate:')
        print(' - You past it without looking back')