with open('testTrees.txt') as trees:
    forestLines = trees.read().split('\n')

forest = []
for line in forestLines:
    treeLine = []
    for tree in line:
        treeLine.append(int(tree))
    forest.append(treeLine)

blankForest = [[0]*len(forest[0]) for _ in range(len(forest))]

print(forest)
print(blankForest)
# 2d list, check each element, if visible have corresponding 2d list element = 1
# check from each direction, solution list will overwrite visible with visible

rotateIterator = 0
xIterator = 0
yIterator = 0
blankForest = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
while rotateIterator < 4:
    print('iteration happened')
    # while yIterator < len(forest) - 1:
    #     xIterator = 0
    #     rowHeight = forest[yIterator][xIterator]
    #     while xIterator < len(forest) - 1:
    #         for x in range(len(forest)):
    #             blankForest[0][xIterator] = 1
    #         if forest[yIterator][xIterator] > rowHeight:
    #             blankForest[yIterator][xIterator] = 1
    #         if forest[yIterator][xIterator] >= rowHeight:
    #             rowHeight = forest[yIterator][xIterator]
    #         xIterator += 1
    #     yIterator += 1
    
    print(blankForest)
    blankForest = [list(row) for row in zip(*reversed(blankForest[::-1]))]
    rotateIterator += 1
    print(blankForest)

print(blankForest)