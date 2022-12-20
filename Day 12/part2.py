from input import map
import sys


def findVal(map: list[list[int]], val: int) -> tuple[int, int]:
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == val:
                return (y, x)
    return None


def findStart(map: list[list[int]]) -> tuple[int, int]:
    return findVal(map, ord("S"))


def findEnd(map: list[list[int]]) -> tuple[int, int]:
    return findVal(map, ord("E"))


def findPath(start, end, map):

    toSearch = [((start), 0)]
    visited = set([start])

    while toSearch:
        node, step = toSearch.pop(0)

        if node == end:
            return step
            exit()
        else:
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nextStep = (node[0] + dx, node[1] + dy)
                if nextStep[0] >= 0 and nextStep[0] < len(map) and nextStep[1] >= 0 and nextStep[1] < len(map[nextStep[0]]):
                    if nextStep not in visited:
                        if map[nextStep[0]][nextStep[1]] - map[node[0]][node[1]] <= 1:
                            toSearch.append((nextStep, step + 1))
                            visited.add(nextStep)

    return sys.maxsize


map = [[ord(c) for c in list(line)] for line in map.split("\n")]

start = findStart(map)
end = findEnd(map)

map[start[0]][start[1]] = ord("a")
map[end[0]][end[1]] = ord("z")

starts = []

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == ord("a"):
            starts.append((y, x))

pathLengths = [findPath((y, x), end, map) for (y, x) in starts]

print(min(pathLengths))
