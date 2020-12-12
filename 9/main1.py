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
    
while whatendposition < len(numbers):
    whatnumber = numbers[whatendposition]
    whatstartposition = whatendposition - 25
    whatslice = numbers[whatstartposition:whatendposition]
    if not lumi_arka_woof(whatnumber, whatslice):
        print(whatnumber)
    whatendposition += 1
print(lumi_arka_calculator)