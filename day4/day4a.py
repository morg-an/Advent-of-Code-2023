with open('input.txt', 'r') as input:
    cards = input.readlines()

def getWinningNums(winNumStrings):
    tempList = []
    for num in winNumStrings:
        if num.isdigit():
            tempList.append(int(num))
    winningNums = set(tempList)
    return winningNums

def getYourNums(yourNumString):
    yourNums = []
    for num in yourNumString:
        if num.isdigit():
            yourNums.append(int(num))
    return yourNums

def scoreCards(cards, winningNums):
    totalScore = 0
    for card in cards:
        matches = 0
        score = 0

        #parce winning and selected numbers from each line
        winNumStrings = card.split("|")[1].strip().replace("  ", " ").split(" ")
        yourNumString = card.split("|")[0].split(":")[1].strip().replace("  ", " ").split(" ")
        
        #return arrays of winning and selected numbers (as int)
        winningNums = getWinningNums(winNumStrings)
        yourNums = getYourNums(yourNumString)

        #compare selected numbers to the winning numbers
        for num in yourNums:
            if num in winningNums:
                matches += 1

        #add card score to total
        if matches >= 1:
            score = 2**(matches-1)
            totalScore += score  

    return totalScore
    
def run():
    winningNums = getWinningNums(cards)
    totalScore = scoreCards(cards, winningNums)
    print(totalScore)

run()