import random
import userInventory

a = '>> '

def pamukTheCat(intelligence):
    print('You distracted by a cat laying on your way:')
    print(' - Pet It (>> 1)')
    print(' - Ask Its Name (>> 2)')
    print(' - Pass (>> P)')
    interaction = input(a)
    if (interaction == '1' and intelligence >= 1):
        print('You pet the cat')
        userInventory.petTheCat()
    elif (interaction == '2' and intelligence >= 5):
        print('You asked for its name:')
        print(' - Its name is Pamuk The Cat')
    elif (interaction == 'P'):
        print('You past it without looking back')
    else:
        print('You are too dumb to communicate:')
        print(' - You past it without looking back')

def wanderingTrader():
    traderOriginList = ['human', 'ork', 'gene']
    humanSellPrice = [2, 2]
    orkSellPrice = [1, 3]
    geneSellPrice = [3, 1]
    traderOrigin = traderOriginList[random.randrange(0,3)]
    print(f'You come to a wanderer {traderOrigin} willing to trade:')
    print(' - Sell (>> 1)')
    print(' - Buy (🔴)')
    print(' - Inventory (>> I)')
    print(' - Pass (>> P)')
    interaction = input(a)
    if (interaction == '1'):
        if (traderOrigin == 'human'):
            print('________SELL________')
            print(f'|  Logs {humanSellPrice[0]}🪙   (>> L) |')
            print(f'| Stones {humanSellPrice[1]}🪙  (>> S) |')
            print('')
        elif (traderOrigin == 'ork'):
            print('________SELL________')
            print(f'|  Logs {orkSellPrice[0]}🪙   (>> L) |')
            print(f'| Stones {orkSellPrice[1]}🪙  (>> S) |')
            print('')
        elif (traderOrigin == 'gene'):
            print('________SELL________')
            print(f'|  Logs {geneSellPrice[0]}🪙   (>> L) |')
            print(f'| Stones {geneSellPrice[1]}🪙  (>> S) |')
            print('')
        materialToSell = input(a)
        if (materialToSell == 'L'):
            if (traderOrigin == 'human'):
                priceMultiplier = humanSellPrice[0]
            elif (traderOrigin == 'ork'):
                priceMultiplier = orkSellPrice[0]
            elif (traderOrigin == 'gene'):
                priceMultiplier = geneSellPrice[0]
            userInventory.trading('log', priceMultiplier)
        elif (materialToSell == 'S'):
            if (traderOrigin == 'human'):
                priceMultiplier = humanSellPrice[1]
            elif (traderOrigin == 'ork'):
                priceMultiplier = orkSellPrice[1]
            elif (traderOrigin == 'gene'):
                priceMultiplier = geneSellPrice[1]
            userInventory.trading('stone', priceMultiplier)
    elif (interaction == 'P'):
        print('You past the wandering trader')

    if (interaction == 'I'):
        userInventory.inventoryVisualizer()
