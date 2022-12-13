from input import crates
import re

[startingStacks, instructions] = crates.split("\n\n")

startingStacks = list(reversed(startingStacks.split("\n")))

stackNums = [int(s) for s in startingStacks[0].split(" ") if s.strip() != '']

stacks = [[] for n in stackNums]
for row in startingStacks[1:]:
    for stack in stackNums:
        crate = row[stack + 3 * (stack - 1)]
        if crate.strip() != '':
            stacks[stack - 1].append(crate)

for instruction in instructions.split("\n"):
    result = re.search(r"^.* (\d+) .* (\d+) .* (\d+).*$", instruction)
    quantity = int(result.group(1))
    fromStack = int(result.group(2))
    toStack = int(result.group(3))

    for i in range(quantity):
        stacks[toStack - 1].append(stacks[fromStack - 1].pop())

for stack in stacks:
    print(stack[-1])
