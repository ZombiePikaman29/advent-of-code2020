f = open("input.txt")
passports = f.read().split("\n\n")
counta = 0


def check_byr(x):
    #(Birth Year) - four digits; at least 1920 and at most 2002.
    if len(x) != 4:
        return False
    x = int(x)
    if x < 1920 or x > 2002:
        return False
    return True

def check_iyr(x):
    #(Issue Year) - four digits; at least 2010 and at most 2020.
    if len(x) != 4:
        return False
    x = int(x)
    if x < 2010 or x > 2020:
        return False
    return True

def check_eyr(x):
    #(Expiration Year) - four digits; at least 2020 and at most 2030.
    if len(x) != 4:
        return False
    x = int(x)
    if x < 2020 or x > 2030:
        return False
    return True

def check_hcl(x):
    #(Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if len(x) != 7:
        return False
    if x[0] != "#":
        return False
    for i in range(1, 7):
        something_else_than_that = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        if x[i] not in something_else_than_that:
            return False
    return True

def check_ecl(x):
    #(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    something_else_than_that = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",]
    if x not in something_else_than_that:
        return False
    return True

def check_pid(x):
    #(Passport ID) - a nine-digit number, including leading zeroes.
    if len(x) != 9:
        return False
    x = int(x)
    return True

def check_hgt(x):
    #(Height) - a number followed by either cm or in:
    #If cm, the number must be at least 150 and at most 193.
    #If in, the number must be at least 59 and at most 76.)
    if len(x) < 4 or len(x) > 5:
        return False
    if len(x) == 4:
        # inches
        numberstring = x[0:2]
        units = x[2:4]
        if units != "in":
            return False
        number = int(numberstring)
        if number < 59 or number > 76:
            return False
    if len(x) == 5:
        # centimetres
        numberstring = x[0:3]
        units = x[3:5]
        if units != "cm":
            return False
        number = int(numberstring)
        if number < 150 or number > 193:
            return False
    return True

for passport in passports:
    induvidual_bits = passport.split()
    print(induvidual_bits)
    dictionary_for_passport = {}
    for induvidual_bit in induvidual_bits:
        k, v = induvidual_bit.split(":")
        dictionary_for_passport[k] = v
    print(dictionary_for_passport)
    try:     
        byr = check_byr(dictionary_for_passport["byr"])
        iyr = check_iyr(dictionary_for_passport["iyr"])
        eyr = check_eyr(dictionary_for_passport["eyr"])
        hcl = check_hcl(dictionary_for_passport["hcl"])
        ecl = check_ecl(dictionary_for_passport["ecl"])
        pid = check_pid(dictionary_for_passport["pid"])
        hgt = check_hgt(dictionary_for_passport["hgt"])
        if byr and iyr and eyr and hcl and ecl and pid and hgt:
            print("Valid")
            counta += 1
    except KeyError:
        pass
    print("--")
print(counta)