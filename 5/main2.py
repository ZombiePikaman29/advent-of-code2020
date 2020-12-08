f = open("input.txt")
seatcodes = f.read().splitlines()
hugeseatID = -1
allseats = list(range(0, 891))
for seatcode in seatcodes:
    binarybleepbloopmalfunction = ""
    for seat in seatcode:
        if seat == "F" or seat == "L":
            binarybleepbloopmalfunction += "0"
        else:
            binarybleepbloopmalfunction += "1"
    print(binarybleepbloopmalfunction)
    rowcode = binarybleepbloopmalfunction[:7]
    columncode = binarybleepbloopmalfunction[7:]
    row = int(rowcode, base=2)
    column = int(columncode, base=2)
    print(row, column)
    seatdadID = row * 8 + column
    print(seatdadID)
    if seatdadID > hugeseatID:
        hugeseatID = seatdadID
    if seatdadID in allseats:
        allseats.remove(seatdadID)
print(hugeseatID) 
print(allseats)