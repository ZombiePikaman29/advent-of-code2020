f = open("input.txt")
lines = f.read().splitlines()
x = 0
y = 0
treeounter = 0
rows = len(lines)
rowlength = len(lines[0])
while y < rows:
    line = lines[y]
    landation = line[x]
    if landation == "#":
        treeounter += 1
    x += 3
    y += 1
    if x >= rowlength:
        x -= rowlength
print(treeounter)