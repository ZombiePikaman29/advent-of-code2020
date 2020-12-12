f = open("input.txt")
numbers = f.read().splitlines()
numbers = [int(x) for x in numbers]
whatendposition = 25
lumi_arka_calculator = 0

def lumi_arka_woof(whatnumber, whatslice):
    global lumi_arka_calculator
    for x in whatslice:
        for y in whatslice:
            if x == y:
                continue
            if (x + y) == whatnumber:
                lumi_arka_calculator += 1
                return True
    
whatnumber = 0

while whatendposition < len(numbers):
    whatnumber = numbers[whatendposition]
    whatstartposition = whatendposition - 25
    whatslice = numbers[whatstartposition:whatendposition]
    if not lumi_arka_woof(whatnumber, whatslice):
        print(whatnumber)
        break
    whatendposition += 1
#print(lumi_arka_calculator)

rowinthelist = 0
while rowinthelist < len(numbers):
    tempstorage = 0
    offset = 0
    minNumber = 999999999999999
    maxNumber = -1
    while True:
        valueofrow = numbers[rowinthelist+offset]
        minNumber = min(minNumber, valueofrow)
        maxNumber = max(maxNumber, valueofrow)
        tempstorage += valueofrow
        if tempstorage == whatnumber:
            print(tempstorage)
            print(minNumber, maxNumber, minNumber+maxNumber)
            exit()
        elif tempstorage > whatnumber:
            break

        offset += 1
        
    rowinthelist += 1