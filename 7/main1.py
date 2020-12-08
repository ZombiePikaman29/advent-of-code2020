f = open("input.txt")
rules = f.read().splitlines()
rulesdictyay = {}
for rule in rules:
    words = rule.split()
    colour = words[0:2]
    colour = " ".join(colour)
    rulesdictyay[colour] = []
    i = 0
    while i < len(words):
        word = words[i]
        try:
            number = int(word)
            firstword = words[i + 1]
            secondword = words[i + 2]
            inside_bag = firstword + " " + secondword
            rulesdictyay[colour].append(inside_bag)
        except ValueError:
            pass
        i += 1

def checkcolour(colour):
    if colour == "shiny gold":
        return True
    inside_bags = rulesdictyay[colour]
    for inside_bag in inside_bags:
        if checkcolour(inside_bag):
            return True
    

valid = []
for bagcolour, colourlist in rulesdictyay.items():
    for colour in colourlist:
        if checkcolour(colour):
            if bagcolour not in valid:
                valid.append(bagcolour)
print(valid)
print(len(valid))