a = '>> '
import time
import random
import globalEvents
import userInventory

print('Enter your user name:')
userName = input(a)

print('')
print('Select difficulty:')
print(' - Easy (>> E)')
print(' - Normal (>> N)')
print(' - Hard (>> H)')

globalDifficulty = input(a)

if (globalDifficulty == 'E') :
    globalDifficulty = 'e'
elif (globalDifficulty == 'N') :
    globalDifficulty = 'n'
elif (globalDifficulty == 'H') :
    globalDifficulty = 'h'
else:
    print('Please input correct to select difficulty')

userTags = []
globalTags = []

userTags.append(userName)
globalTags.append(globalDifficulty)

userPower = 0
userIntelligence = 0

print('')
print('Select origin:')
print(' - Human (>> H)')
print(' - Ork (>> O)')
print(' - Gene (>> G)')
userOrigin = input(a)

if (userOrigin == 'H') :
    userOrigin = 'h'
    userPower = 5
    userIntelligence = 5
elif (userOrigin == 'O') :
    userOrigin = 'o'
    userPower = 9
    userIntelligence = 1
elif (userOrigin == 'G') :
    userOrigin = 'g'
    userPower = 1
    userIntelligence = 9

userTags.append(userOrigin)
userTags.append(userPower)
userTags.append(userIntelligence)

time.sleep(1)

print('')
print('Skill exps you gained from origin:')
print(' - Power: ' + str(userPower) + ' 💪 exp')
print(' - Intelligence: ' + str(userIntelligence) + ' 💡 exp')

time.sleep(1)
#globalEvents.tree(userTags[2], globalTags[0])
#globalEvents.rock(userTags[2], globalTags[0])
#globalEvents.camp(userIntelligence)
#globalEvents.person(0, userIntelligence)
print(f'''
You started your journey {userTags[0]}. 
In the Wonderful world of Survival On Terminal. 
You have {userTags[2]} experience of power. You have {userTags[3]} experience of intelligence. 
Get ready for the journey...''')
time.sleep(2)

while True:
    print('-------------')
    print('Travelling...')
    print('-------------')
    time.sleep(3)
    eventNumber = random.randrange(0, 6)
    if (eventNumber == 0):
        globalEvents.tree(userTags[2], globalTags[0])
    elif (eventNumber == 1):
        globalEvents.rock(userTags[2], globalTags[0])
    elif (eventNumber == 2):
        globalEvents.camp(userTags[3])
    elif (eventNumber == 3):
        globalEvents.person(0, userTags[3])
    elif (eventNumber == 4):
            globalEvents.stone(userTags[3])
    elif (eventNumber == 4):
                globalEvents.stone(userTags[3])