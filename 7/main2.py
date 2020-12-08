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
            colour_arka_count = (inside_bag, number)
            rulesdictyay[colour].append(colour_arka_count)
        except ValueError:
            pass
        i += 1

calculata_lumi = 0

def getbags(colour):
    global calculata_lumi
    inside_bags= rulesdictyay[colour]
    calculata_lumi += 1
    for inside_bag, count in inside_bags:
        for i in range(count):
            getbags(inside_bag)


shiny_gold_bags_inside = rulesdictyay["shiny gold"]

for colour, count in shiny_gold_bags_inside:
    for i in range(count):
        getbags(colour)
print(calculata_lumi)