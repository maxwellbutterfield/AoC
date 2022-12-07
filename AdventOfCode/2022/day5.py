import numpy as np

with open('CraneInstructions.txt') as craneInstructions:
    rawMoves = craneInstructions.read()
rawMovesLines = rawMoves.split('\n')

moves = []
for x in range(len(rawMovesLines)):
    moves.append(rawMovesLines[x].split(' '))

with open('Crates.txt') as newCrates:
    rawCrates = newCrates.read()
rawCratesLines = rawCrates.split('\n')

rawCratesLines.pop(-1) # get rid of numbers at bottom of crates data
rawCratesLines.reverse()

crates = []
for line in rawCratesLines:
    line = line[1:]
    column = []
    while len(line) > 1:
        column.append(line[0])
        line = line[4:]
    crates.append(column)
crates = np.transpose(crates).tolist()

for rowNum in range(len(crates)):
    for x in range(len(crates[0])):
        if crates[rowNum][-1] == ' ':
            crates[rowNum].pop()

for move in moves:
    numTimes = int(move[1])
    crateFrom = int(move[3]) - 1
    crateTo = int(move[5]) - 1
    # while numTimes > 0:
    #     crates[crateTo].append(crates[crateFrom][-1])
    #     crates[crateFrom].pop()
    #     numTimes -= 1
    crates[crateTo] = crates[crateTo] + crates[crateFrom][len(crates[crateFrom])-numTimes:]
    crates[crateFrom] = crates[crateFrom][:len(crates[crateFrom])-numTimes]

for x in range(len(crates)):
    print(crates[x][-1])