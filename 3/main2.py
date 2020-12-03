f = open("input.txt")
lines = f.read().splitlines()
rows = len(lines)
rowlength = len(lines[0])
total = 1
mooooooooovements = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
for mooooooooovement in mooooooooovements:
    x = 0
    y = 0
    treeounter = 0

    while y < rows:
        line = lines[y]
        landation = line[x]
        if landation == "#":
            treeounter += 1
        x += mooooooooovement[0]
        y += mooooooooovement[1]
        if x >= rowlength:
            x -= rowlength
    print(treeounter)
    total *= treeounter
    print(total)