from input import packets

# packets = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]"""


def parsePacketList(p: str):
    packetStack = []
    packet = []
    for i in range(len(p)):
        if p[i].isdigit():
            packetStack[-1].append(int(p[i]))
        elif p[i] == '[':
            newList = []
            if packetStack:
                packetStack[-1].append(newList)
            packetStack.append(newList)
        elif p[i] == ']':
            packet = packetStack.pop()
    return packet


def packetsInOrder(left: list, right: list):
    for i in range(len(left)):
        if i == len(right):
            return False
        if type(left[i]) is int and type(right[i]) is int:
            if left[i] == right[i]:
                continue
            return left[i] < right[i]
        elif type(left[i]) is list and type(right[i]) is list:
            return packetsInOrder(left[i], right[i])
        elif type(left[i]) is list and type(right[i]) is int:
            return packetsInOrder(left[i], [right[i]])
        elif type(left[i]) is int and type(right[i]) is list:
            return packetsInOrder([left[i]], right[i])

    return len(left) <= len(right)


parsedPackets = [(parsePacketList(p.split("\n")[0]),
                  parsePacketList(p.split("\n")[1])) for p in packets.split("\n\n")]

answer = 0
for i, packetPair in enumerate(parsedPackets):
    if packetsInOrder(packetPair[0], packetPair[1]):
        answer += i + 1

print(answer)
