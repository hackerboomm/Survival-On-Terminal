userInventory = [0, 0, 'null', 'null']
materials = ['null', 'stoneAxe', 'stonePickaxe']
#loglar 0. elementte
#rocklar 1. elementte

multiplier = 0


def getLog(difficulty):
    if (difficulty == 'e'):
        multiplier = 3
    elif (difficulty == 'n'):
        multiplier = 2
    elif (difficulty == 'h'):
        multiplier = 1

    userInventory[0] += multiplier
    print(' - +' + str(multiplier) + ' logs')

def getRock(difficulty):
    if (difficulty == 'e'):
        multiplier = 3
    elif (difficulty == 'n'):
        multiplier = 2
    elif (difficulty == 'h'):
        multiplier = 1

    userInventory[1] += multiplier
    print(' - +' + str(multiplier) + ' stones')

def crafting(material):
    logCount = userInventory[0]
    rockCount = userInventory[1]
    if (material == '1' and logCount >= 1 and rockCount >= 2):
        userInventory[2] = str(materials[int(material)])
        print(' - + Stone Axe')
        userInventory[0] -= 1
        print(' - -1 log')
        userInventory[1] -= 2
        print(' - -2 rocks')
    elif (material == '2' and logCount >= 1 and rockCount >= 3):
        userInventory[3] = str(materials[int(material)])
        print(' - + Stone Pickaxe')
        userInventory[0] -= 1
        print(' - -1 log')
        userInventory[1] -= 3
        print(' - -3 rocks')
    else:
        print('You dont have enough resources to craft')


