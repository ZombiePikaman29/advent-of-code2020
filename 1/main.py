f = open("input.txt")
r = f.read().splitlines()
for a in r:
    ai = int(a)
    #answer = 2020 - ai
    #print(ai, answer)
    for b in r:
        bi = int(b)
        for c in r:
            ci = int(c)

            if ai + bi + ci == 2020:
                print(ai, bi, ci, ai+bi+ci, ai * bi * ci)