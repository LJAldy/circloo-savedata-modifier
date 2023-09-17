coordline = "b"
listcoord = []
while coordline != "":
    coordline = input("Enter coords: ")
    listcoord.append(coordline)
listcoord.pop(len(listcoord)-1)
startnumber = int(input("Start number: ")) - 1
loops = 2*int(input("Portals length: "))
loopnum = 0
while loopnum < loops:
    if loopnum % 2 == 1:
        listcoord[loopnum] = "< " + str(startnumber)
    else:
        coordword = []
        lastwordend = 0
        for letter in range(len(listcoord[loopnum])):
            if listcoord[loopnum][letter] == " ":
                coordword.append(listcoord[loopnum][lastwordend:letter])
                lastwordend = letter + 1
        coordword.append(listcoord[loopnum][lastwordend:len(listcoord[loopnum])])
        if coordword[0] in ["portal","mc","c"]:
            coordword[1] = float(coordword[1]) + 35

        fullline = ""
        for word in coordword:
            fullline += str(word) + " "
        listcoord.append(fullline)
        listcoord.append("< " + str(startnumber))
        startnumber += 1
    loopnum += 1
for line in listcoord:
    print(line)
input()