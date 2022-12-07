import string

with open('Rucksacks.txt') as inputRucks:
    jumbledRucks = inputRucks.read()

bunchedRucks = jumbledRucks.split()

groupedRucks = []
while len(bunchedRucks) > 2:
    groupedRucks.append((bunchedRucks[0], bunchedRucks[1], bunchedRucks[2]))
    bunchedRucks = bunchedRucks[3:len(bunchedRucks)]
    
badges = []
for party in groupedRucks:
    for firstOne in party[0]:
        if firstOne in party[1]:
            if firstOne in party[2]:
                badges.append(firstOne)
                break
print(badges)



# separatedRucks = []
# for x in bunchedRucks:
#     firstHalf, secondHalf = x[:len(x)//2], x[len(x)//2:len(x)]
#     separatedRucks.append((firstHalf, secondHalf))

# misplaced = []
# for y in separatedRucks:
#     for z in y[0]:
#         if z in y[1]:
#             misplaced.append(z)
#             break

priority = dict.fromkeys(string.ascii_lowercase, 0)
upperDict = dict.fromkeys(string.ascii_uppercase, 0)
priority.update(upperDict)
counter = 1
for j in priority:
    priority[j] = counter
    counter += 1

# totalPriority = 0
# for k in misplaced:
#     totalPriority += priority[k]

totalPriority = 0
for k in badges:
    totalPriority += priority[k]


print(totalPriority)