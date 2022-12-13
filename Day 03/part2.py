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
groups = zip(*(iter(rucksacks.split("\n")),) * 3)
print(sum([priorities[next(iter(set(group[0]) & set(group[1]) & set(group[2])))]
           for group in groups]))
