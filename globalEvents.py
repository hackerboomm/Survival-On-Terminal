a = '>> '

import userInventory

def tree(power, difficulty):
    print('You came across a tree:')
    print(' - Cut (>> C)')
    print(' - Pass (>> P)')
    interaction = input(a)
    if (interaction == 'C' and power >= 5):
        print('You cut the tree:')
        userInventory.getLog(difficulty)
    elif (interaction == 'C' and power < 5):
        print('You have not enough guts to cut it:')
        print(' - You past the tree leaving behind')
    elif (interaction == 'P'):
        print('You past the tree')

def rock(power, difficulty):
    print('You came across a rock:')
    print(' - Break (>> B)')
    print(' - Pass (>> P)')
    interaction = input(a)
    if (interaction == 'B' and power >= 5):
        print('You break the rock:')
        userInventory.getRock(difficulty)
    elif (interaction == 'B' and power < 5):
        print('You have not enough guts to break it:')
        print(' - You past the rock leaving behind')
    elif (interaction == 'P'):
        print('You past the rock')