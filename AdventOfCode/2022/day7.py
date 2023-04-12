with open('FileStructure.txt') as inputFileCommands:
    fileCommands = inputFileCommands.read().split('\n')

class node:
    def __init__(self, name, level, parent, fileType, value, height):
        self.name = name
        self.level = level
        self.parent = parent
        self.fileType = fileType # options = directory, file
        self.value = value # value = 0 if not a file
        self.height = height

listOfNodes = {}
parentIndex = []
parentTree = []
currentLevel = 0
numDirs = 0

for line in fileCommands:
    lineData = line.split(' ')
    if lineData[0] == '$':
        if lineData[1] == 'cd': # directory changing commands
            if lineData[2] == '/': # root directory special case
                values = node(''.join(parentTree) + lineData[2], currentLevel, 'root', 'directory', 0, len(parentTree))
                # print(''.join(parentTree) + lineData[2])
                listOfNodes.update({''.join(parentTree) + lineData[2]: values})
                parentIndex.append(0)
                parentTree.append(lineData[2])
                currentLevel += 1 # ready for next level
                numDirs += 1
            elif lineData[2] == '..':
                currentLevel -= 1 # move up a level
                parentIndex.pop()
                parentTree.pop()
            else:
                values = node(''.join(parentTree) + lineData[2], currentLevel, parentTree[-1], 'directory', 0, len(parentTree))
                # print(''.join(parentTree) + lineData[2])
                listOfNodes.update({''.join(parentTree) + lineData[2]: values})
                parentIndex.append(len(listOfNodes))
                parentTree.append(lineData[2])
                currentLevel += 1
        # do nothing if lineData[0] == 'ls'
    elif lineData[0].isnumeric() == True:
        values = node(''.join(parentTree) + lineData[1], currentLevel, parentTree[-1], 'file', int(lineData[0]), len(parentTree))
        # print(''.join(parentTree) + lineData[1])
        listOfNodes.update({''.join(parentTree) + lineData[1]: values})
    elif lineData[0] == 'dir':
        numDirs += 1

lastHeight = 0
counter = 0
runningTotals = [0]*numDirs
indexOfTotals = []

for x in listOfNodes.values():
    # print('\n' + str(x.name))
    # print("x's height is: " + str(x.height))
    # print('last height was: ' + str(lastHeight))
    # print(indexOfTotals)
    if x.height > lastHeight:
        # print('in first if case')
        lastHeight = x.height
        
        indexOfTotals.append(counter)
        counter += 1
    elif x.height < lastHeight:
        # print('in second if case')
        numLevels = lastHeight - x.height
        lastHeight = x.height
        # counter += 1
        for y in range(numLevels):
            indexOfTotals.pop()
    
    # print(indexOfTotals)

    if x.value > 0:
        for y in indexOfTotals:
            # print(y)
            runningTotals[y] += x.value

# print(runningTotals)

sumTotals = 0
for x in runningTotals:
    if x <= 100000:
        sumTotals += x

# print(sumTotals)

fullTotal = 0
for x in runningTotals:
    fullTotal += x

emptySpace = 70000000 - max(runningTotals)
# print(emptySpace)

neededSpace = 30000000 - emptySpace

candidates = []
for x in runningTotals:
    if x > neededSpace:
        candidates.append(x)

print(min(candidates))