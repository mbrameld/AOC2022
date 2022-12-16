from input import program
import re

program = re.split(r' |\n', program)

x = 1
adding = False
interesting = []
for i in range(1, 221):
    if i == 20 or (i - 20) % 40 == 0:
        interesting.append(i * x)
    if adding:
        x += int(program[i-1])
        adding = False
    elif program[i-1] == 'addx':
        adding = True

print(interesting)
print(sum(interesting))
