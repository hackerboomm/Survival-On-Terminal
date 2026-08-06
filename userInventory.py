userInventory = [0, 0]

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


logCount = userInventory[0]
rockCount = userInventory[1]
