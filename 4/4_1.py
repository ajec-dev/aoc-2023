with open('input_4.txt', 'r') as file:
    lines = [l.strip() for l in file.readlines()]

sum = 0;
for game in lines:
    info, numbers = game.split(':')
    winning, mine = numbers.split('|')
    winners = set(winning.strip().split()).intersection(mine.strip().split())
    numWinners = len(winners)
    score = 0 if len(winners) == 0 else pow(2, numWinners - 1)
    sum += score
print(sum)