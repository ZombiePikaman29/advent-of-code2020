f = open("input.txt")
groups = f.read().split("\n\n")
total_of_totals = 0
for group in groups:
    memory = []
    total = 0
    for letter in group:
        if letter == "\n":
            continue
        if letter not in memory:
            memory.append(letter)
            total += 1
    total_of_totals += total
    print(total_of_totals)