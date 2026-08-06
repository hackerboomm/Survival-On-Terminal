a = '>> '
import time

print('Enter your user name:')
userName = input(a)

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

userTags = []
globalTags = []

userTags.append(userName)
globalTags.append(globalDifficulty)

userPower = 0
userIntelligence = 0

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

print('Skill exps you gained from origin:')
print(' - Power: ' + str(userPower) + ' exp')
print(' - Intelligence: ' + str(userIntelligence) + ' exp')

print(userTags)
print(globalTags)

print('You came on a tree:')
print(' - Cut (>> C)')
print(' - Pass (>> P)')
interaction = input(a)

if (interaction == 'C' and userTags[2] >= 5):
    print('Trying to cut the tree...')
    time.sleep(2)
    print('You cut the tree:')
    print(' - Log')
elif (interaction == 'C' and userTags[2] < 5):
    print('Trying to cut the tree...')
    time.sleep(2)
    print('Your power was not enough.')
    print(' - You pass the tree')
elif (interaction == 'P'):
    print('You pass the tree')