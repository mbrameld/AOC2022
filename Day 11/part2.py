from __future__ import annotations
from input import monkies
from math import floor
from functools import reduce
from operator import mul

# monkies = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""


class Monkey:
    def __init__(self, startingItems: list[int], operation: str, divisor: int, targets: dict[bool, int]):
        self.items = startingItems
        self.operation = operation
        self.divisor = divisor
        self.targets = targets
        self.itemsInspected = 0

    def catch(self, item: int):
        self.items.append(item)

    def inspectAndThrow(self, monkies: dict[int, Monkey], modulo: int):
        while (len(self.items) > 0):
            item = self.items.pop(0)
            item = eval(self.operation, {"old": item}) % modulo
            self.itemsInspected += 1
            monkies[self.targets[item % self.divisor == 0]].catch(item)


parsedMonkies: list[Monkey] = []
for monkey in monkies.split("\n\n"):
    monkey = [l.strip() for l in monkey.split('\n')]
    startingItems = [int(i)
                     for i in monkey[1].split(':')[1].strip().split(", ")]
    operation = monkey[2].split(' = ')[1]
    divisor = int(monkey[3].split('by ')[1])
    trueTarget = int(monkey[4][-1])
    falseTarget = int(monkey[5][-1])
    parsedMonkies.append(Monkey(startingItems, operation, divisor, {
                         True: trueTarget, False: falseTarget}))

# had to google for this trick
modulo = 1
for monkey in parsedMonkies:
    modulo *= monkey.divisor

for roundNum in range(1, 10001):
    if roundNum % 10 == 0:
        print(f"Round {roundNum}")
    for monkeyNum, monkey in enumerate(parsedMonkies):
        monkey.inspectAndThrow(parsedMonkies, modulo)

    # print(f"After round {roundNum}:")
    # for i, monkey in enumerate(parsedMonkies):
    #     print(f"    Monkey {i}: {monkey.itemValues()}")
    # print()

# for i, monkey in enumerate(parsedMonkies):
#     print(f"Monkey {i} inspected items {monkey.countItemsInspected()} times.")

print(reduce(mul, list(
    reversed(sorted([m.itemsInspected for m in parsedMonkies])))[:2]))
