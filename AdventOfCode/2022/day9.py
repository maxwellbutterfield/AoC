with open('testRopeMoves.txt') as newRopeMoves:
    ropeMoves = newRopeMoves.read().split('\n')

head = [0][0]
tail = [0][0]

head[0, 0] = 1
tail[0, 0] = 1
print(head[0][0])
print(tail[0][0])
# headIndexX = 0
# headIndexY = 0
# for moveLine in ropeMoves:
#     move = moveLine.split(' ')
#     if move[0] == 'R':
#         try:
#             head[headIndexY, headIndexX + 1] = 1
#         except IndexError:

#     elif move[0] == 'L':
#     elif move[0] == 'U':
#     elif move[0] == 'D':