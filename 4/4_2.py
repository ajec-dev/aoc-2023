import itertools

with open('input_4.txt', 'r') as file:
    lines = [l.strip() for l in file.readlines()]

sum = 0;
buffer = [1] * len(lines) # start with 1 copy of each card
for idx, game in enumerate(lines):
    info, numbers = game.split(':')
    winning, mine = numbers.split('|')
    winners = set(winning.strip().split()).intersection(mine.strip().split())
    numWinners = len(winners)
    multiplier = buffer.pop(0)
    extraCards = [multiplier] * numWinners
    buffer = [x + y for x, y in itertools.zip_longest(extraCards, buffer, fillvalue = 0)]
    sum += multiplier
print(sum)