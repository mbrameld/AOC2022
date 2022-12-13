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

c = 0
for instruction in instructions.split("\n"):
    result = re.search(r"^.* (\d+) .* (\d+) .* (\d+).*$", instruction)
    quantity = int(result.group(1))
    fromStack = int(result.group(2)) - 1
    toStack = int(result.group(3)) - 1

    cratesToMove = stacks[fromStack][-quantity:]
    stacks[fromStack] = stacks[fromStack][:len(stacks[fromStack]) - quantity]
    stacks[toStack] = stacks[toStack] + cratesToMove


for stack in stacks:
    print(stack[-1])
