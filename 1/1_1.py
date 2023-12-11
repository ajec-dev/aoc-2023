with open('input_1.txt', 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    chars = list(line)
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