from anytree import Node, RenderTree

with open('testFileStructure.txt') as inputFileCommands:
    fileCommands = inputFileCommands.read().split('\n')

parentList = []
parentIndex = 0
files = {}
for line in fileCommands:
    lineData = line.split(' ')
    print(lineData)
    if lineData[0] == '$':
        if lineData[1] == 'cd': # change directory 
            if lineData[2] == '/':
                globals()[lineData[2]] = Node(lineData[2])
                parentList.append(lineData[2])
                parentIndex = 0
            elif lineData[2] == '..':
                    parentIndex -= 1
            else:
                print(parentList)
                print(parentIndex)
                globals()[lineData[2]] = Node(lineData[2],parent=parentList[parentIndex])
                parentList.append(lineData[2])
                parentIndex += 1
        # if lineData[1] == 'ls':
        #     break
    # if lineData[0] == 'dir':
    #     break
    elif type(lineData[0]) == int:
        globals()[lineData[1]] = Node(lineData[1],parent=parentList[parentIndex])
        files.update({lineData[1]:lineData[0]})
# print(RenderTree('/'))