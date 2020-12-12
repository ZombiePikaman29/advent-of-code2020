import copy

f = open("input.txt")
lines = f.read().splitlines()

instructions = []

for line in lines:
    operation, numbastring = line.split()
    numba = int(numbastring)
    instructions.append([operation, numba])

brokenInstruction = 0
attempta = 0
while brokenInstruction < len(instructions):
    tempInstructions = copy.deepcopy(instructions)

    while True:
        operation, numba = tempInstructions[brokenInstruction]
        if operation == 'acc':
            brokenInstruction += 1
        elif operation == 'jmp':
            tempInstructions[brokenInstruction][0] = 'nop'
            brokenInstruction += 1
            break
        elif operation == 'nop':
            tempInstructions[brokenInstruction][0] = 'jmp'
            brokenInstruction += 1
            break

    pos = 0
    acc = 0
    while True:
        if pos >= len(tempInstructions):
            print(acc, attempta)
            exit()
        if tempInstructions[pos] == None:
            break

        operation, numba = tempInstructions[pos]
        tempInstructions[pos] = None
        if operation == "acc":
            acc += numba
            pos += 1
        elif operation == "jmp":
            pos += numba
        elif operation == "nop":
            pos += 1
    attempta += 1