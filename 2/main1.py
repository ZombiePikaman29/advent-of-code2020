f = open("input.txt")
lines = f.read().splitlines()
passwordcounter = 0
for line in lines:
    parts = line.split()
    count1, count2 = parts[0].split('-')
    print(line, count1, count2)
    count1 = int(count1)
    count2 = int(count2)
    blob = parts[1][0]
    print(blob)
    password = parts[2]
    foundulator = password.count(blob)
    if foundulator >= count1 and foundulator <= count2:
        passwordcounter = passwordcounter + 1
print(passwordcounter)