import os
print("Current Directory: ", os.getcwd())
os.chdir('/home/morgan/Documents/_Programming/challenges/Advent-of-Code-2023/day2')

with open("input.txt", "r") as input:
    games = input.readlines()

print(os.getcwd())

# set bag contents
RED_CUBES = 12
BLUE_CUBES = 14
GREEN_CUBES = 13

# returns [[game number, [maxRed, maxBlue, maxGreen]], ... ]
def parceString(games):
    gameArray = []
    for game in games:
        gameNum = int(game.split(":")[0].removeprefix('Game '))
        gameResultsString = game.split(":")[1].removesuffix('\n')
        gameResultsArray = gameResultsString.split(";")
        redBlueGreen = parceGameResultsArray(gameResultsArray)
        gameArray.append([gameNum, redBlueGreen])
    return(gameArray)

def parceGameResultsArray(gameArray):
    redBlueGreen = [0,0,0]
    for draw in gameArray:
        colors = draw.split(",")
        for color in colors:
            if "red" in color:
                numRed = int("".join(filter(str.isdigit, color)))
                if numRed > redBlueGreen[0]:
                    redBlueGreen[0] = numRed
            if "blue" in color:
                numBlue = int("".join(filter(str.isdigit, color)))
                if numBlue > redBlueGreen[1]:
                    redBlueGreen[1] = numBlue
            if "green" in color:
                numGreen = int("".join(filter(str.isdigit, color)))
                if numGreen > redBlueGreen[2]:
                    redBlueGreen[2] = numGreen
    return redBlueGreen

def findPossibleGames(games):
    sumOfIDs = 0
    for game in games:
        #print("Game:", game)
        if game[1][0] > RED_CUBES:
            #print("Too many red cubes.", game[1][0], "of", RED_CUBES )
            sumOfIDs += 0
        elif game[1][1] > BLUE_CUBES:
            #print("Too many blue cubes.", game[1][1], "of", BLUE_CUBES )
            sumOfIDs += 0
        elif game[1][2] > GREEN_CUBES:
            #print("Too many green cubes.", game[1][2], "of", GREEN_CUBES )
            sumOfIDs += 0
        else:
            sumOfIDs += game[0]
            #print("Running Total: ", sumOfIDs, "(added ", game[0],")")
    return sumOfIDs

def run():
    parcedData = parceString(games)
    print(findPossibleGames(parcedData))

run()