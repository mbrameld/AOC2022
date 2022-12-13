from input import assignments

enclosuresCount = 0
for assignment in assignments.split("\n"):
    [elf1, elf2] = assignment.split(",")
    [start1, end1] = [int(s) for s in elf1.split("-")]
    [start2, end2] = [int(s) for s in elf2.split("-")]

    #      start1
    # start2    end2

    if (start2 <= start1 <= end2):
        enclosuresCount += 1
        continue

    # start1    end1
    #      start2
    if (start1 <= start2 <= end1):
        enclosuresCount += 1
        continue

print(enclosuresCount)
