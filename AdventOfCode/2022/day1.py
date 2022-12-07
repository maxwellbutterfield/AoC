with open('Calories.txt') as inputCalories:
    rawCalories = inputCalories.read()

bunchedCalories = []
bunchedCalories = rawCalories.split("\n\n")

separatedCalories = []
for x in range(len(bunchedCalories)):
    separatedCalories.append(bunchedCalories[x].split("\n"))

summedCalories = []
for y in range(len(separatedCalories)):
    tempForCasting = []
    for z in range(len(separatedCalories[y])):
        tempForCasting.append(int(separatedCalories[y][z]))
    summedCalories.append(sum(tempForCasting))

topThreeCaloriesSum = 0
i = 0
while i < 3:
    maxValue1 = max(summedCalories)
    topThreeCaloriesSum += maxValue1
    summedCalories.pop(summedCalories.index(maxValue1))
    i += 1

print(topThreeCaloriesSum)