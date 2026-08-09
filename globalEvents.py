a = '>> '

import userInventory
import globalPersons

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

<<<<<<< Updated upstream
=======
def stone(power):
    print('You came across a stone:')
    print(' - Collect (>> C)')
    print(' - Pass (>> P)')
    interaction = input(a)
    if (interaction == 'C' and power >= 1):
        print('You collect the stone:')
        userInventory.getStone()
    elif (interaction == 'C' and power < 1):
        print('You have not enough guts to collect it:')
        print(' - You past the stone leaving behind')
    elif (interaction == 'P'):
        print('You past the stone')

def stick(power):
    print('You came across a stick:')
    print(' - Collect (>> C)')
    print(' - Pass (>> P)')
    interaction = input(a)
    if (interaction == 'C' and power >= 1):
        print('You collect the stick:')
        userInventory.getStick()
    elif (interaction == 'C' and power < 1):
        print('You have not enough guts to collect it:')
        print(' - You past the stick leaving behind')
    elif (interaction == 'P'):
        print('You past the stick')

>>>>>>> Stashed changes
def camp(intelligence):
    print('You found a camp:')
    print(' - Crafting (>> C)')
    print(' - Inventory (>> I)')
    print(' - Pass (>> P)')
    interaction = input(a)
    def craftingMenu():
        print(''' - Select To Craft
     * Stone Axe (>> 1)
     * Stone Pickaxe (>> 2)''')
        craftSelect = input(a)
        if (craftSelect == '1' and intelligence >= 1):
            userInventory.crafting('1')
        elif (craftSelect == '2' and intelligence >= 5):
            userInventory.crafting('2')
        else:
            print('You are so dumb to craft:')
            print(' - You past the camp feeling upset about yourself')
    if (interaction == 'C'):
        print('You opened crafting menu:')
        craftingMenu()
    elif (interaction == 'I'):
        userInventory.inventoryVisualizer()
    elif (interaction == 'P'):
        print('You past the camp without doing something')

def person(personNumber, intelligence):
    if (personNumber == 0):
        globalPersons.pamukTheCat(intelligence)
    elif (personNumber == 1):
        globalPersons.wanderingTrader()
