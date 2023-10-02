def displaygrid(gridded,usegridded):
    for linenum in range(len(gridded)):
        printline = ""
        line = grid[linenum]
        for pointnum in range(len(line)):
            point = gridded[linenum][pointnum]
            printline += point
        for pointnum in range(len(line)):
            point = usegridded[linenum][pointnum]
            printline += point
        print(printline)
choice = "a"
while choice not in ("0","1","2"):
    choice = input("Choose an option:\n[0] Excel Spreadsheet Input\n[1] Ascii Image Input\n[2] Raw Grid Input\n : ")
dataline = "b"
listdata = []
while dataline != "":
    dataline = input("Enter data: ")
    listdata.append(dataline + " ")
listdata.pop(len(listdata)-1)
startnumber = int(input("Start number: "))
startx = int(input("X start: "))
starty = int(input("Y start: "))
pixelwidth = int(input("Pixel width: "))
transx = 0
transy = 0
grid = []
width = 0
for dataline in listdata:
    if len(dataline) > width:
        width = len(dataline)
if choice == "0":
    for dataline in listdata:
        gridline = []
        prevtab = True
        for char in dataline:
            #print(char, prevtab)
            if char == "1":
                gridline.append("#")
                prevtab = False
            else:
                if prevtab:
                    gridline.append(" ")
                else:
                    prevtab = True
        grid.append(gridline)
elif choice == "1":
    for dataline in listdata:
        gridline = []
        for charnum in range(width):
            if charnum >= len(dataline):
                gridline.append(" ")
            else:
                if dataline[charnum] == " ":
                    gridline.append(" ")
                else:
                    gridline.append("#")
        grid.append(gridline)
elif choice == "2":
    for dataline in listdata:
        gridline = []
        for charnum in range(width):
            gridline.append(dataline[charnum])
print(grid)
for line in grid:
    printline = ""
    for point in line:
        printline += point
    print(printline)
    if len(printline) > width:
        width = len(printline)
for linenum in range(len(grid)):
    printline = ""
    line = grid[linenum]
    for pointnum in range(len(line)):
        point = grid[linenum][pointnum]
        printline += point
    print(printline)
usedpoints = [row[:] for row in grid.copy()]
circode = []
for linenum in range(len(grid)):
    line = grid[linenum]
    for pointnum in range(len(line)):
        point = line[pointnum]
        circodeline = "b "
        if point == "#" and usedpoints[linenum][pointnum] == "#":
            usedpoints[linenum][pointnum] = " "
            unitwidth = 1
            unitheight = 1
            looping = True
            #print(linenum,unitwidth,pointnum, width, len(line),grid[linenum][pointnum],pointnum+linenum < width+1,usedpoints[linenum][pointnum],)
            while looping:
                if (pointnum+unitwidth) < (width+1):
                    if grid[linenum][pointnum+unitwidth] == "#":
                        #print(usedpoints[linenum])
                        usedpoints[linenum][pointnum+unitwidth] = " "
                        unitwidth += 1
                    else:
                        looping = False
                else:
                    looping = False
            looping = True
            #displaygrid(grid,usedpoints)
            #print(linenum,unitwidth,pointnum, width, len(line),grid[linenum][pointnum],usedpoints[linenum][pointnum])
            while looping:
                for index in range(unitwidth):
                    if linenum+unitheight < len(grid) and pointnum+index < width:
                        #print(linenum,unitheight,pointnum,index,unitwidth, width, len(line))
                        if not grid[linenum+unitheight][pointnum+index] == "#":
                            looping = False
                    else:
                        looping = False
                if looping:
                    for index in range(unitwidth):
                        usedpoints[linenum+unitheight][pointnum+index] = " "
                    unitheight += 1
            #print(startx,transx,pixelwidth,unitwidth,starty,transy,pixelwidth,unitheight)
            circodeline += str(startx+transx+(pixelwidth * unitwidth - 1)/2) + " " + str(starty+transy+(pixelwidth * unitheight - 1)/2) + " "
            circodeline += str((pixelwidth * unitwidth)/2) + " " + str((pixelwidth * unitheight)/2) + " 0"
            circode.append(circodeline)
            circode.append("< " + str(startnumber))
            startnumber += 1
        transx += pixelwidth
    transy += pixelwidth
    transx = 0
'''
for gluenum in range(startnumber-1):
    circode.append("/ GLUE " + str(gluenum) + " " + str(gluenum + 1))
    circode.append("< " + str(startnumber))
    startnumber += 1
'''
pause = 0
for line in circode:
    print(line)
    pause += 1
    if pause % 1000 == 0:
        input()
#'''