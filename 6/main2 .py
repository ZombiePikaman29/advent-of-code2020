f = open("input.txt")
groups = f.read().split("\n\n")
total_of_totals = 0
for group in groups:
    lines_of_group = len(group.splitlines())
    memory = []
    total = 0
    for letter in group:
        if letter == "\n":
            continue
        if group.count(letter) == lines_of_group:
            if letter not in memory:
                memory.append(letter)
                total += 1

        

    total_of_totals += total
    print(total, total_of_totals)