with open('Passwords.txt', 'r') as f:
    for line in f:
        splitLine = line.split()
newDict[int(splitLine[0])] = ",".join(splitLine[1:])

