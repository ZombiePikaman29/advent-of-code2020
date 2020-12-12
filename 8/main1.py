f = open("input.txt")
lines = f.read().splitlines()

instructions = []

for line in lines:
    operation, numbastring = line.split()
    numba = int(numbastring)
    instructions.append([operation, numba])
pos = 0
acc = 0
while True:
    if instructions[pos] == None:
        break

    operation, numba = instructions[pos]
    instructions[pos] = None
    if operation == "acc":
        acc += numba
        pos += 1
    elif operation == "jmp":
        pos += numba
    elif operation == "nop":
        pos += 1

print(acc)