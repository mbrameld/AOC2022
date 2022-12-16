from input import moves

# moves = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""


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

    if tail[0] == head[0] - 2 and tail[1] == head[1] - 2:
        return (tail[0] + 1, tail[1] + 1)
    if tail[0] == head[0] + 2 and tail[1] == head[1] + 2:
        return (tail[0] - 1, tail[1] - 1)
    if tail[0] == head[0] + 2 and tail[1] == head[1] - 2:
        return (tail[0] - 1, tail[1] + 1)
    if tail[0] == head[0] - 2 and tail[1] == head[1] + 2:
        return (tail[0] + 1, tail[1] - 1)

    return tail


def moveRope(rope):
    newRope = [rope[0]]
    for i in range(1, len(rope)):
        newRope.append(moveTail(newRope[i-1], rope[i]))
    return newRope


def drawRope(rope):
    for y in reversed(range(-5, 16)):
        line = []
        for x in range(-11, 15):
            if (y, x) not in rope:
                if (y, x) == (0, 0):
                    line.append("s")
                else:
                    line.append(".")
            else:
                idx = rope.index((y, x))
                if idx == 0:
                    line.append("H")
                elif idx == len(rope) - 1:
                    line.append("T")
                else:
                    line.append(str(idx))
        print(''.join(line))
    print()


rope = [(0, 0)] * 10
visited = set([rope[-1]])
drawRope(rope)

for move in moves.split("\n"):
    [direction, count] = move.split(" ")
    for i in range(int(count)):
        match direction:
            case "R":
                rope[0] = (rope[0][0], rope[0][1] + 1)
            case "L":
                rope[0] = (rope[0][0], rope[0][1] - 1)
            case "U":
                rope[0] = (rope[0][0] + 1, rope[0][1])
            case "D":
                rope[0] = (rope[0][0] - 1, rope[0][1])
        rope = moveRope(rope)
        visited.add(rope[-1])
    # drawRope(rope)

print(len(visited))
