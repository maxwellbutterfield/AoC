with open('Campsites.txt') as inputCampsites:
    campsites = inputCampsites.read()
assignments = campsites.split('\n')

#split by ',' then split by '-'

counter = 0
# for x in assignments:
#     dividedAssignments = x.split(',')
#     comparison = []
#     for y in dividedAssignments:
#         comparison.append(y.split('-'))
#     if (int(comparison[0][0]) <= int(comparison[1][0])) and (int(comparison[0][1]) >= int(comparison[1][1])):
#         counter += 1
#     elif (int(comparison[0][0]) >= int(comparison[1][0])) and (int(comparison[0][1]) <= int(comparison[1][1])):
#         counter += 1

# print(counter)

for x in assignments:
    dividedAssignments = x.split(',')
    comparison = []
    for y in dividedAssignments:
        comparison.append(y.split('-'))
    if (int(comparison[0][1]) < int(comparison[1][0])):
        counter += 1
    elif (int(comparison[1][1]) < int(comparison[0][0])):
        counter += 1

print(len(assignments) - counter)


# [0] [1]
# [0] [1]