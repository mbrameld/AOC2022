from input import assignments

enclosuresCount = 0
for assignment in assignments.split("\n"):
    [elf1, elf2] = assignment.split(",")
    [start1, end1] = elf1.split("-")
    [start2, end2] = elf2.split("-")
    if (int(start2) >= int(start1) and int(end2) <= int(end1)) or (int(start1) >= int(start2) and int(end1) <= int(end2)):
        enclosuresCount += 1
print(enclosuresCount)
