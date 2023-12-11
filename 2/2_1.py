from functools import reduce

limits = {'red': 12, 'green': 13, 'blue': 14}

with open('input_2.txt', 'r') as file:
    lines = file.readlines()

def add_group(groupDict: dict[str, int], rawGroupInfo: str):
    groupCount, groupKey = rawGroupInfo.strip().split(' ')
    groupDict[groupKey] = int(groupCount)
    return groupDict

def check_round(groupDict):
    for item in limits.items():
        if dict(groupDict).get(item[0], 0) > item[1]:
            return 0
    return 1

def check_rounds(rounds: list[str]):
    checked = reduce(lambda acc, cur: acc * check_round(reduce(add_group, cur.strip().split(','), dict())), rounds, 1)
    return checked;

sum = 0
for line in lines:
    workingLine = str(line)
    gameInfo, roundInfo = workingLine.split(':')
    gameNum = int(gameInfo.replace('Game', '').strip())
    rounds = roundInfo.split(';')
    checkedGame = check_rounds(rounds);
    sum = sum + (gameNum * checkedGame)
print(sum)