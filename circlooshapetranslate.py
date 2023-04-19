coordline = "b"
listcoord = []
while coordline != "":
    coordline = input("Enter coords: ")
    listcoord.append(coordline)
listcoord.pop(len(listcoord)-1)
startnumber = int(input("Start number: "))
transx = int(input("X translation: "))
transy = int(input("Y translation: "))
for counter in range(len(listcoord)):
    if counter % 2 == 0:
        listcoord[counter] = "< " + str(startnumber)
        startnumber += 1
    else:
        coordword = []
        lastwordend = 0
        for letter in range(len(listcoord[counter])):
            if listcoord[counter][letter] == " ":
                coordword.append(listcoord[counter][lastwordend:letter])
                lastwordend = letter + 1
        coordword.append(listcoord[counter][lastwordend:len(listcoord[counter])])
        if coordword[0] == "b" or coordword[0] == "c" or coordword[0] == "rc" or coordword[0] == "mc" or coordword[0] == "mb":
            coordword[1] = float(coordword[1]) + transx
            coordword[2] = float(coordword[2]) + transy
        elif coordword[0] == "l_at":
            coordword[1] = float(coordword[1]) + transx
            coordword[2] = float(coordword[2]) + transy
            coordword[3] = float(coordword[3]) + transx
            coordword[4] = float(coordword[4]) + transy
        elif coordword[0] == "t" or coordword[0] == "mt":
            coordword[1] = float(coordword[1]) + transx
            coordword[2] = float(coordword[2]) + transy
            coordword[3] = float(coordword[3]) + transx
            coordword[4] = float(coordword[4]) + transy
            coordword[5] = float(coordword[5]) + transx
            coordword[6] = float(coordword[6]) + transy
        fullline = ""
        for word in coordword:
            fullline += str(word) + " "
        listcoord[counter] = fullline
for line in listcoord:
    print(line)
input()
