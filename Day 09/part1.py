from input import moves


def moveTail(head, tail):
    if tail[0] == head[0] and tail[1] == head[1] - 2:
        return (tail[0], head[1] - 1)
    if tail[0] == head[0] and tail[1] == head[1] + 2:
        return (tail[0], head[1] + 1)
    if tail[0] == head[0] - 2 and tail[1] == head[1]:
        return (tail[0] + 1, head[1])
    if tail[0] == head[0] + 2 and tail[1] == head[1]:
        return (tail[0] - 1, head[1])

    if tail[0] == head[0] - 2 and abs(tail[1] - head[1]) == 1:
        return (tail[0] + 1, head[1])
    if tail[0] == head[0] + 2 and abs(tail[1] - head[1]) == 1:
        return (tail[0] - 1, head[1])
    if abs(tail[0] - head[0]) == 1 and tail[1] == head[1] - 2:
        return (head[0], tail[1] + 1)
    if abs(tail[0] - head[0]) == 1 and tail[1] == head[1] + 2:
        return (head[0], tail[1] - 1)

    return tail


head = (0, 0)
tail = (0, 0)
visited = set([tail])

for move in moves.split("\n"):
    [direction, count] = move.split(" ")
    for i in range(int(count)):
        match direction:
            case "R":
                head = (head[0], head[1] + 1)
            case "L":
                head = (head[0], head[1] - 1)
            case "U":
                head = (head[0] + 1, head[1])
            case "D":
                head = (head[0] - 1, head[1])
        tail = moveTail(head, tail)
        visited.add(tail)

print(len(visited))
