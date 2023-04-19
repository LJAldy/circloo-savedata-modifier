characters = {
    "0" : [16,"b 1308 1401 8 1 0","b 1315 1412 1 12 0","b 1301 1412 1 12 0","b 1308 1423 8 1 0"],
    "1" : [16,"b 1308 1423 8 1 0","b 1308 1412 1 12 0","b 1304.50 1401 4.50 1 0"],
    "2" : [16,"b 1308 1401 8 1 0","b 1308 1423 8 1 0","b 1308 1412 8 1 0","b 1301 1417.50 1 6.50 0","b 1315 1406.50 1 6.50 0"],
    "3" : [16,"b 1308 1401 8 1 0","b 1315 1412 1 12 0","b 1308 1423 8 1 0","b 1308 1412 8 1 0"],
    "4" : [16,"b 1308 1416 8 1 0","b 1313 1412 1 12 0","b 1301 1408.50 1 8.50 0"],
    "5" : [16,"b 1308 1401 8 1 0","b 1308 1423 8 1 0","b 1308 1409 8 1 0","b 1301 1405 1 5 0","b 1308 1409 8 1 0"],
    "6" : [16,"b 1308 1401 8 1 0","b 1308 1423 8 1 0","b 1308 1412 8 1 0","b 1315 1417.50 1 6.50 0","b 1301 1412 1 12 0"],
    "7" : [16,"b 1308 1401 8 1 0","b 1315 1412 1 12 0","b 1311 1412 5 1 0"],
    "8" : [16,"b 1308 1401 8 1 0","b 1315 1412 1 12 0","b 1301 1412 1 12 0","b 1308 1423 8 1 0","b 1308 1412 8 1 0"],
    "9" : [16,"b 1308 1401 8 1 0","b 1315 1412 1 12 0","b 1301 1406.50 1 6.50 0","b 1308 1423 8 1 0","b 1308 1412 8 1 0"],
    "." : [2,"b 1301 1424 1 1 0"],
    "A" : [16],
    "B" : [16],
    "C" : [16],
    "D" : [16],
    "E" : [16],
    "F" : [16],
    "G" : [16],
    "H" : [16],
    "I" : [16],
    "J" : [16],
    "K" : [16],
    "L" : [16],
    "M" : [16],
    "N" : [16],
    "O" : [16],
    "P" : [16],
    "Q" : [16],
    "R" : [16],
    "S" : [16,"b 1308 1401 8 1 0","b 1308 1412 8 1 0","b 1308 1423 8 1 0","b 1301 1406.50 1 6.50 0","b 1315 1417.50 1 6.50 0"],
    "T" : [16,"b 1308 1401 8 1 0","b 1308 1412 1 12 0"],
    "U" : [16],
    "V" : [16],
    "W" : [16],
    "X" : [16],
    "Y" : [16],
    "Z" : [16]
}

translate = input("Text: ")
xstart = int(input("TSX: "))
xend = int(input("TEX: "))
ystart = int(input("TSY: "))
size = int(input("Size: "))
datanum = int(input("Start: "))
shapestomake = []
xbegin = xstart
for char in translate:
    lettershape = characters[char]
    shapenum = 0
    for shape in lettershape:
        if type(shape) == int:
            width = shape
        else:
            coordword = []
            lastwordend = 0
            for letter in range(len(shape)):
                if shape[letter] == " ":
                    coordword.append(shape[lastwordend:letter])
                    lastwordend = letter + 1
            coordword.append(shape[lastwordend:len(shape)])
            if coordword[0] == "b":
                coordword[1] = float(coordword[1])-float(coordword[3]) #repos coord start to topleft
                coordword[2] = float(coordword[2])-float(coordword[4])
                coordword[3] = float(coordword[3]) * 2 * size
                coordword[4] = float(coordword[4]) * 2 * size
                coordword[1] = (coordword[1] - 1300) * size + xstart #reset coord, resize, repos to next char
                coordword[2] = (coordword[2] - 1400) * size + ystart
            for valueindex in range(len(coordword)):
                num = coordword[valueindex]
                if str(num)[len(str(num))-2:] == ".0":
                    coordword[valueindex] = str(num)[:len(str(num))-2] # remove decimal on floats
            shapestomake.append(str(coordword))
        shapenum += 1
    xstart += (width + 4) * size
    if xstart > xend: # newline
        xstart = xbegin
        ystart += 28 * size
for shapenum in range(len(shapestomake)):
    for cleanchar in "'[],":
        shapestomake[shapenum] = shapestomake[shapenum].replace(cleanchar,"")
for shape in shapestomake:
    print("> " + str(datanum))
    print(shape)
    datanum += 1
