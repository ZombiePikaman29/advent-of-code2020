f = open("input.txt")
passports = f.read().split("\n\n")
counta = 0
for passport in passports:
    print(passport)
    byr = "byr" in passport
    iyr = "iyr" in passport
    eyr = "eyr" in passport
    hgt = "hgt" in passport
    hcl = "hcl" in passport
    ecl = "ecl" in passport
    pid = "pid" in passport
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        counta += 1
        print("Valid")
    print("--")
print(counta)