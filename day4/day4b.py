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
    scoreArray = []
    for card in cards:
        matches = 0

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

        scoreArray.append(matches)
    return scoreArray

def countCards(scoreArray):
    totalCards = 0

    #create an array for keeping track of additional cards - initial setup in same size as the score array
    print("Score Array: ", scoreArray)

    bonusCards = []
    i = 0
    while i < len(scoreArray):
        bonusCards.append(0)
        i += 1

    i = 0
    while i < len(scoreArray):
        currentCardScore = scoreArray[i]
        currentBonusCards = bonusCards[i]
        totalCards += 1+currentBonusCards #adds the current card you are scoring to the total, along with previously earned bonus cards
        print("Running Total: ", totalCards)
        if currentCardScore > 0:
            print("Card at i = ", i, "is > 0. ("+ str(currentCardScore)+")")
            j = 1
            while j <= currentCardScore: #updates the bonus card table each time a new card is analyzed
                bonusCards[i+j] += 1+currentBonusCards 
                j += 1
        print("New Score Array: ", scoreArray)
        print("New Bonus Array: ", bonusCards)
        i += 1
    return totalCards

def run():
    winningNums = getWinningNums(cards)
    scoreArray = scoreCards(cards, winningNums)
    answer = countCards(scoreArray)
    print(answer)

run()