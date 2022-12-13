from input import rucksacks

priorities = {}
priority = 1
for c in [chr(asc) for asc in range(ord("a"), ord("z") + 1)]:
    priorities[c] = priority
    priority += 1
for c in [chr(asc) for asc in range(ord("A"), ord("Z") + 1)]:
    priorities[c] = priority
    priority += 1

allPriorities = 0
for sack in rucksacks.split("\n"):
    compartment1 = set(sack[:int(len(sack) / 2)])
    compartment2 = set(sack[int(len(sack) / 2):])
    common = compartment1.intersection(compartment2)
    allPriorities += priorities[next(iter(common))]

print(allPriorities)
