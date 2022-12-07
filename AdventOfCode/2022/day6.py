with open('Datastream.txt') as bits:
    datastream = bits.read()

flag = False
length = 14 # 4 for part 1
counter = 14 # 4 for part 1
while flag != True:
    for sequence in datastream[counter-length:counter]:
        unique = list(set(datastream[counter-length:counter]))
        if len(unique) > 13:
            print(counter)
            flag = True
            break
        else:
            counter += 1