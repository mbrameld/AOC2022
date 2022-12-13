from input import elves

currentElfCount = 0
maxElfCount = -1
for entry in elves.split("\n"):
    if entry == "":
        maxElfCount = max(maxElfCount, currentElfCount)
        currentElfCount = 0
    else:
        currentElfCount += int(entry)
print(maxElfCount)
