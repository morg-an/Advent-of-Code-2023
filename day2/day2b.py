with open("input.txt", "r") as input:
    games = input.readlines()

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

def calcPowers(games):
    sumOfPowers = 0
    for game in games:
        power = game[1][0]*game[1][1]*game[1][2]
        sumOfPowers += power
    return sumOfPowers

def run():
    parcedData = parceString(games)
    sumOfPowers = calcPowers(parcedData)
    print(sumOfPowers)

run()