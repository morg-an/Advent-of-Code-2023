import os
print("Current Directory: ", os.getcwd())

with open('input.txt', 'r') as input:
    engine = input.read()

lines = engine.split('\n')

#function retruns [[character coordinates][partNumber, [row, column]]]
def mapEngine(lines):
    engineSchematic = [[],[]]
    row = 0
    for line in lines:
        column = 0
        enginePart = ""
        for char in line:
            if char.isdigit():
                enginePart += char
                column += 1
            else:
                if enginePart != "":
                    engineSchematic[1].append([int(enginePart), [row, column-1]]) #records the part number and the ending location of the number on the engine schematic
                    enginePart = ""
                if char == ".":
                    column += 1
                else:
                    engineSchematic[0].append([row, column]) #records the location of the special char on the engine schematic
                    column += 1
        if enginePart != "": #account for engine part at the end of a line
            engineSchematic[1].append([int(enginePart), [row, column-1]])
        row += 1
    print(engineSchematic)
    return(engineSchematic)

def findParts(engine):
    partsTotal = 0
    for part in engine[1]:

        #set values
        partNum = part[0]
        numDigits = len(str(part[0]))
        row = part[1][0]
        column = part[1][1]

        #find adjacent values
        adjacent = findAdjacent(row, column, numDigits)
        print("Part", partNum, "Adjacent:", adjacent)

        #compare adjacent values to known character coordinates
        for coordinate in adjacent:
            if coordinate in engine[0]:
                partsTotal += partNum
                print("Adjacent Char Found! ", partNum, "added to total. New total:", partsTotal)
                break
    return partsTotal

def findAdjacent(row, column, numDigits):
    adjacent = []
    adjacent.append([row, column+1]) #right
    adjacent.append([row, column-numDigits]) #left
    i = 0
    while i < numDigits:
        adjacent.append([row-1, column-i]) #directly above each digit
        adjacent.append([row+1, column-i]) #directly below each digit
        i += 1
    adjacent.append([row-1, column+1]) #right-upper diagonal
    adjacent.append([row+1, column+1]) #right-lower diagonal
    adjacent.append([row-1, column-numDigits]) #left-upper diagonal
    adjacent.append([row+1, column-numDigits]) #left lower diagonal
    return adjacent

def run():
    engineSchematic = mapEngine(lines)
    answer = findParts(engineSchematic)
    print(answer)

run()