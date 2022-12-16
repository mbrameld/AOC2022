from input import program
import re

program = re.split(r' |\n', program)

x = 1
adding = False
interesting = []
line = []
for i in range(0, 240):
    pixelX = (i) % 40
    if pixelX >= x - 1 and pixelX <= x + 1:
        line.append('#')
    else:
        line.append('.')
    if (len(line) == 40):
        print(''.join(line))
        line = []
    if adding:
        x += int(program[i])
        adding = False
    elif program[i] == 'addx':
        adding = True
