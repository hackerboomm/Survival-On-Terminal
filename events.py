import items as it
import persons as pr
import player as pl

itemType = ["log", "stick"]
personType = [""]

def switchInventory():
    print(f"""
    | {pl.playerStats[0]}'s Inventory:
    |------------------------------- 
    | Wood: {pl.playerInventory[0]}
    |------------------------------- 
    | > CLOSE (Will pass the item/person)
    """)

def itemEventString(type):
    print(f"""
    | You came along a {type}!
    | What will you do:
    |------------------------------- 
    | > GATHER
    | > PASS
    | > INVENTORY
    """)

def itemEvent(type, command):

    if (type == "log" and command == "gather"):
        pl.playerInventory[0] += it.log["value"]
    elif (type == "stick" and command == "gather"):
        pl.playerInventory[0] += it.stick["value"]

    if (command == "inventory"):
        switchInventory()

def personEventString(type):
    print(f"""
    | You came across a {type}
    | What will you do:
    |-------------------------------
    | > COMMUNICATE
    | > PASS
    | > INVENTORY
    """)

def personEvent(type, command):
    print("Person event started...")

