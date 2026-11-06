playerStats = []
playerInventory = [0]
playerRaces = ["human", "ork", "gene"]

humanStats = [5, 5]
orkStats = [9, 1]
geneStats = [1, 9]

def raceStatsIntegrater(raceValue):
    if (raceValue == "human"):
        playerStats.extend(humanStats)
    elif (raceValue == "ork"):
        playerStats.extend(orkStats)
    elif (raceValue == "gene"):
         playerStats.extend(geneStats)

