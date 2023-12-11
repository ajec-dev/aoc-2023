from functools import reduce

with open('input_2.txt', 'r') as file:
    lines = file.readlines()

def add_group(groupDict: dict[str, int], rawGroupInfo: str):
    groupCount, groupKey = rawGroupInfo.strip().split(' ')
    groupDict[groupKey] = int(groupCount)
    return groupDict

def check_minimums(minimums, groupDict):
    for item in minimums.items():
        key = item[0]
        currentMin = item[1]
        groupMin = groupDict.get(item[0])
        if groupMin is not None:
            if currentMin is None:
                minimums[key] = groupMin
            else:
                minimums[key] = max(currentMin, groupMin)
    return minimums

def get_power(rounds: list[str]):
    minimums = {'red': None, 'green': None, 'blue': None}
    for round in rounds:
        groupDict = reduce(add_group, round.strip().split(','), dict())
        minimums = check_minimums(minimums, groupDict)
    return reduce(lambda acc, cur: acc * cur, minimums.values(), 1)

sum = 0
for line in lines:
    workingLine = str(line)
    gameInfo, roundInfo = workingLine.split(':')
    gameNum = int(gameInfo.replace('Game', '').strip())
    rounds = roundInfo.split(';')
    power = get_power(rounds);
    sum = sum + power
print(sum)