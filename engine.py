import player as pl
import events as ev
import random
import time

a = "    > "

#-------------------------INTRODUCTION STAGE-------------------------------
print("""
    | Welcome to the wonderful world of
    | Survival on Terminal
    | What's your name Adventurer?
""")

playerName = input(a)
pl.playerStats.append(playerName)


playerRace = ""
while (playerRace not in pl.playerRaces):
    print(f"""
    | What a nice name {playerName}!
    | Now your past belongs to you
    | What is your race to play?
    |------------------------------- 
    | (Hint: There are three races: 
    | Human, Ork, Gene)
    """)

    playerRace = input(a)
    if (playerRace.lower() in pl.playerRaces and playerRace.lower() not in pl.playerStats):
        pl.playerStats.append(playerRace.lower())
        pl.raceStatsIntegrater(playerRace.lower())
        break
    else:
            print(f"""
    | We don't have any {playerRace.capitalize()} race here.
                    """)

while (playerRace == pl.playerRaces):
    print("test")

print(f"""
    | According to your race ({playerRace.capitalize()}):
    |   Your power: {pl.playerStats[2]}
    |   Your Intelligence: {pl.playerStats[3]}
""")
#--------------------------------------------------------------------------

#-------------------------GAME ENGINE STAGE--------------------------------

while (True):
    timerValue = random.randrange(1, 4)
    print(f"""
    | Travelling...
    |-------------------------------
    | Player Data: 
    | Profile: {playerName}
    | Profile Race: {playerRace.capitalize()}
    | Power: {pl.playerStats[2]}
    | Intelligence: {pl.playerStats[3]}
    """)
    time.sleep(timerValue)

    eventValue = random.randrange(0, 11)
    if (eventValue <= 3):
         print(f"""
    | You came across a person
    """)
    elif (eventValue > 3):
         itemEventValue = random.randrange(0,2)
         ev.itemEventString(ev.itemType[itemEventValue])
         commandInput = input(a)
         ev.itemEvent(ev.itemType[itemEventValue], commandInput.lower())
         if (commandInput.lower() == "inventory"):
              commandInput = input(a)

#--------------------------------------------------------------------------
