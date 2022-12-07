with open('RPSdata.txt') as rawStrategyGuide:
    strategyGuide = rawStrategyGuide.read()

rounds = strategyGuide.split('\n')

totalScore = 0
# A = Rock
# B = Paper
# C = Scissors

# X = Rock = 1 pt
# Y = Paper = 2 pts
# Z = Scissors = 3 pts

# Win = 6 pts
# Draw = 3 pts

# for x in range(len(rounds)):
#     battle = rounds[x].split(' ')
#     if battle[0] == 'A': # opponent threw rock
#         if battle[1] == 'X': # you throw rock
#             totalScore += 1 # 1 pt for rock
#             totalScore += 3 # 3 pts for draw
#         elif battle[1] == 'Y': # you throw paper
#             totalScore += 2 # 2 pts for paper
#             totalScore += 6 # 6 pts for win
#         elif battle [1] == 'Z':
#             totalScore += 3 # 3 pts for scissors
#             totalScore += 0 # 0 pts for lose
#     elif battle[0] == 'B': # opponent thew paper
#         if battle[1] == 'X': # you throw rock
#             totalScore += 1 # 1 pt for rock
#             totalScore += 0 # 0 pts for lose
#         elif battle[1] == 'Y': # you throw paper
#             totalScore += 2 # 2 pts for paper
#             totalScore += 3 # 3 pts for draw
#         elif battle [1] == 'Z':
#             totalScore += 3 # 3 pts for scissors
#             totalScore += 6 # 6 pts for win
#     elif battle[0] == 'C': # opponent thew scissors
#         if battle[1] == 'X': # you throw rock
#             totalScore += 1 # 1 pt for rock
#             totalScore += 6 # 6 pts for win
#         elif battle[1] == 'Y': # you throw paper
#             totalScore += 2 # 2 pts for paper
#             totalScore += 0 # 0 pts for lose
#         elif battle [1] == 'Z':
#             totalScore += 3 # 3 pts for scissors
#             totalScore += 3 # 3 pts for draw

for x in range(len(rounds)):
    battle = rounds[x].split(' ')
    if battle[0] == 'A': # opponent threw rock
        if battle[1] == 'X': # you need to lose
            totalScore += 3 # 3 pts for scissors
            totalScore += 0 # 0 pts for lose
        elif battle[1] == 'Y': # you need to draw
            totalScore += 1 # 1 pt for rock
            totalScore += 3 # 3 pts for draw
        elif battle [1] == 'Z': # you need to win
            totalScore += 2 # 2 pts for paper
            totalScore += 6 # 6 pts for win
    elif battle[0] == 'B': # opponent thew paper
        if battle[1] == 'X': # you need to lose
            totalScore += 1 # 1 pt for rock
            totalScore += 0 # 0 pts for lose
        elif battle[1] == 'Y': # you need to draw
            totalScore += 2 # 2 pts for paper
            totalScore += 3 # 3 pts for draw
        elif battle [1] == 'Z': # you need to win
            totalScore += 3 # 3 pts for scissors
            totalScore += 6 # 6 pts for win
    elif battle[0] == 'C': # opponent thew scissors
        if battle[1] == 'X': # you need to lose
            totalScore += 2 # 2 pts for paper
            totalScore += 0 # 0 pts for lose
        elif battle[1] == 'Y': # you need to draw
            totalScore += 3 # 3 pts for scissors
            totalScore += 3 # 3 pts for draw
        elif battle [1] == 'Z': # you need to win
            totalScore += 1 # 1 pt for rock
            totalScore += 6 # 6 pts for win

print(totalScore)