f = open("input.txt")
lines = f.read().splitlines()
passwordcounter = 0
for line in lines:
    parts = line.split()
    pos1, pos2 = parts[0].split('-')
    print(line, pos1, pos2)
    pos1 = int(pos1) - 1
    pos2 = int(pos2) - 1
    blob = parts[1][0]
    print(blob)
    password = parts[2]
    ch1 = password[pos1]
    ch2 = password[pos2]
    print(ch1, ch2)
    if (blob == ch1 and blob != ch2) or (blob != ch1 and blob == ch2):
        passwordcounter += 1
        print("Valid")
    else:
        print("Invalid")
print(passwordcounter)