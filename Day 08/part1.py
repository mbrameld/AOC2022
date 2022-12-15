from input import trees

visible = set()

treeGrid = [[int(h) for h in line] for line in trees.split('\n')]

for y in range(len(treeGrid)):
    tallest = -1
    for x in range(len(treeGrid[y])):
        if treeGrid[y][x] > tallest:
            visible.add((y, x))
            tallest = treeGrid[y][x]
    tallest = -1
    for x in reversed(range(len(treeGrid[y]))):
        if treeGrid[y][x] > tallest:
            visible.add((y, x))
            tallest = treeGrid[y][x]

for x in range(len(treeGrid[0])):
    tallest = -1
    for y in range(len(treeGrid)):
        if treeGrid[y][x] > tallest:
            visible.add((y, x))
            tallest = treeGrid[y][x]
    tallest = -1
    for y in reversed(range(len(treeGrid))):
        if treeGrid[y][x] > tallest:
            visible.add((y, x))
            tallest = treeGrid[y][x]

print(len(visible))
