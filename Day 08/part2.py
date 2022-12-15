from input import trees
from functools import reduce
from operator import mul


def countTreesInView(grid, y, x):
    treesInView = [0, 0, 0, 0]
    # check up
    for y2 in reversed(range(y)):
        treesInView[0] += 1
        if grid[y2][x] >= grid[y][x]:
            break
    # check down
    for y2 in range(y+1, len(grid)):
        treesInView[1] += 1
        if grid[y2][x] >= grid[y][x]:
            break
    # check left
    for x2 in reversed(range(x)):
        treesInView[2] += 1
        if grid[y][x2] >= grid[y][x]:
            break
    # check right
    for x2 in range(x+1, len(grid[y])):
        treesInView[3] += 1
        if grid[y][x2] >= grid[y][x]:
            break

    return reduce(mul, treesInView)


treeGrid = [[int(h) for h in line] for line in trees.split('\n')]

mostTreesInView = -1
for y in range(len(treeGrid)):
    for x in range(len(treeGrid[y])):
        treesVisibleFromHere = countTreesInView(treeGrid, y, x)
        if treesVisibleFromHere > mostTreesInView:
            mostTreesInView = treesVisibleFromHere

print(mostTreesInView)
