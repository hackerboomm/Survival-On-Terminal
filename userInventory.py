userInventory = [0, 0, 'null', 'null', 0]
materials = ['null', 'stoneAxe', 'stonePickaxe']
#loglar 0. elementte
#rocklar 1. elementte
#coinler 4. elemntte

multiplier = 0

def inventoryVisualizer():
    logs = userInventory[0]
    stones = userInventory[1]
    coins = userInventory[4]

    print(f'''
    🎒 INVENTORY 🎒
                  
| - {logs} 🪵       
| - {stones} 🪨     
| ------------------
| - {coins} 🪙      
                  
''')

def getLog(difficulty):
    if (difficulty == 'e'):
        multiplier = 3
    elif (difficulty == 'n'):
        multiplier = 2
    elif (difficulty == 'h'):
        multiplier = 1

    if (userInventory[2] == 'stoneAxe'):
        multiplier = multiplier + 2

    userInventory[0] += multiplier
    print(' - +' + str(multiplier) + ' logs')

def getRock(difficulty):
    if (difficulty == 'e'):
        multiplier = 3
    elif (difficulty == 'n'):
        multiplier = 2
    elif (difficulty == 'h'):
        multiplier = 1

    if (userInventory[3] == 'stonePickaxe'):
            multiplier = multiplier + 2

    userInventory[1] += multiplier
    print(' - +' + str(multiplier) + ' stones')

def getStick():
    userInventory[0] += 1
    print(' - +1 logs 🪵')

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

def trading(material, multiplier):
    logCount = userInventory[0]
    rockCount = userInventory[1]
    if (material == 'log' and logCount >= 1):
        userInventory[0] -= 1
        print(' - -1 log 🪵')
        userInventory[4] += multiplier
        print(f' - +{multiplier} coin(s) 🪙')
    elif (material == 'stone' and rockCount >= 1):
        userInventory[1] -= 1
        print(' - -1 stone 🪨')
        userInventory[4] += multiplier
        print(f' - +{multiplier} coin(s) 🪙')

def petTheCat():
    print(' - +1 coin 🪙')
    userInventory[4] += 1
    


