from input import elves

currentElfCount = 0
elfCounts = []
for entry in elves.split("\n"):
    if entry == "":
        elfCounts.append(currentElfCount)
        currentElfCount = 0
    else:
        currentElfCount += int(entry)

print(sum(list(reversed(sorted(elfCounts)))[:3]))
