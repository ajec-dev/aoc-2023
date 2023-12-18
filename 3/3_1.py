import functools

def is_symbol(char):
    return not (char.isalnum() or char == '.')

def contains_symbol(neighborhood: list[str]):
    return any(is_symbol(c) for c in neighborhood)

with open('input_3.txt', 'r') as file:
    lines = [l.strip() for l in file.readlines()]

lineLength = len(lines[0])
allChars = functools.reduce(lambda acc, cur: acc + cur, lines, '')

sum = 0
foundNum = ''
foundIdx = -1
keepNum = False
for idx, char in enumerate(allChars):
    lineStart = idx % lineLength == 0
    lineEnd = idx % lineLength == (lineLength - 1)
    if char.isnumeric():
        if foundNum == '':
            foundIdx = idx
            if not lineStart and is_symbol(allChars[idx - 1]):
                keepNum = True
        foundNum += char
        if lineEnd:
            if keepNum != True:
                upperStart = idx - lineLength - len(foundNum)
                lowerStart = idx + lineLength - len(foundNum)
                upperNeighbors = '' if upperStart < 0 else list(allChars)[upperStart:upperStart + len(foundNum)]
                lowerNeighbors = '' if lowerStart > len(allChars) else list(allChars)[lowerStart:lowerStart + len(foundNum)]
                keepNum = contains_symbol(upperNeighbors) or contains_symbol(lowerNeighbors)
            if keepNum == True:
                sum += int(foundNum)
            foundNum = ''
            foundIdx = -1
            keepNum = False
    else:
        if foundNum != '':
            if is_symbol(char):
                keepNum = True
            if keepNum != True:
                upperStart = foundIdx - lineLength - 1
                lowerStart = foundIdx + lineLength - 1
                upperEnd = idx - lineLength + 1
                lowerEnd = idx + lineLength + 1
                upperNeighbors = '' if upperStart < 0 else list(allChars)[upperStart : upperEnd]
                lowerNeighbors = '' if lowerStart > len(allChars) else list(allChars)[lowerStart : lowerEnd]
                keepNum = contains_symbol(upperNeighbors) or contains_symbol(lowerNeighbors)
            if keepNum == True:
                sum += int(foundNum)
            foundNum = ''
            foundIdx = -1
            keepNum = False
print(sum)