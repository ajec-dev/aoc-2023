import functools
import itertools

def take_nums(chars, reverse = False):
    if reverse == True:
        workingChars = list(reversed(chars))
        return ''.join(reversed(list(itertools.takewhile(str.isnumeric, workingChars))))
    else:
        return ''.join(itertools.takewhile(str.isnumeric, chars))

with open('input_3.txt', 'r') as file:
    lines = [l.strip() for l in file.readlines()]

lineLength = len(lines[0])
allChars = functools.reduce(lambda acc, cur: acc + cur, lines, '')

sum = 0
foundNum = ''
foundIdx = -1
keepNum = False
for idx, char in enumerate(allChars):
    isGear = char == "*"
    if isGear:
        isLineStart = idx % lineLength == 0
        isLineEnd = idx % lineLength == (lineLength - 1)
        
        startIdx = int(idx / lineLength) * lineLength
        
        charAbove = '' if idx < lineLength else allChars[idx - lineLength]
        charBelow = '' if idx + lineLength > len(allChars) else allChars[idx + lineLength]

        neighbors = list()

        if not isLineStart and allChars[idx - 1].isnumeric():
            neighbors.append(take_nums(allChars[startIdx : idx], True))

        if not isLineEnd and allChars[idx + 1].isnumeric():
            neighbors.append(take_nums(allChars[idx + 1 : startIdx + lineLength]))

        # check neighborhood above gear
        if charAbove != '':
            beforeAbove = '' if isLineStart else take_nums(allChars[startIdx - lineLength : idx - lineLength], True)
            afterAbove = '' if isLineEnd else take_nums(allChars[idx - lineLength + 1 : startIdx])
            if charAbove.isnumeric():
                neighbors.append(beforeAbove + charAbove + afterAbove)
            else:
                neighbors.extend(filter(lambda s: s != '', [beforeAbove, afterAbove]))

        # check neighborhood below gear
        if charBelow != '':
            beforeBelow = '' if isLineStart else take_nums(allChars[startIdx + lineLength : idx + lineLength], True)
            afterBelow = '' if isLineEnd else take_nums(allChars[idx + lineLength + 1 : startIdx + 2 * lineLength])
            if charBelow.isnumeric():
                neighbors.append(beforeBelow + charBelow + afterBelow)
            else:
                neighbors.extend(filter(lambda s: s != '', [beforeBelow, afterBelow]))

        if len(neighbors) == 2:
            sum += int(neighbors[0]) * int(neighbors[1])
print(sum)
