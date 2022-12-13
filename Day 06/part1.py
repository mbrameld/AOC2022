from input import message

sequenceLength = 4

charsChecked = sequenceLength
while charsChecked < len(message):
    seq = message[charsChecked-sequenceLength:charsChecked]
    if len(set(seq)) == sequenceLength:
        print(charsChecked)
        exit()
    charsChecked += 1
print("None")
