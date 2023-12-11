from functools import reduce

numberWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numberWordValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
1.  Locate index of every number in the provided string
2.  Locate start index of every number word in the provided string
3.  Sort (1) and (2) by lowest index, and build new string containing only numbers from the provided string,
    replacing number words with corresponding numbers
"""
def process_line_new(line): 
    workingLine = str(line)
    numberIndices = list()
    for charIdx, char in enumerate(workingLine):
        if char.isnumeric():
            numberIndices.append([charIdx, char])
    for wordIdx, numberWord in enumerate(numberWords):
        repeat = True
        workingIdx = 0
        while repeat:
            repeat = False    
            findIdx = workingLine.find(numberWord, workingIdx)
            if findIdx > -1:
                repeat = True
                numberIndices.append([findIdx, str(numberWordValues[wordIdx])])
                workingIdx = findIdx + len(numberWord)
    newList = sorted(numberIndices, key = lambda index: index[0])
    return reduce(lambda s, item: s + item[1], newList, '')

with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    workingLine = process_line_new(line)
    chars = list(workingLine)
    first = ''
    last = ''
    for startChar in chars:
        if startChar.isdigit():
            first = startChar
            break
    for endChar in reversed(chars):
        if endChar.isdigit():
            last = endChar
            break
    sum = sum + int(first + last)
print('sum: ' + str(sum))
