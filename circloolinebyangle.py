import math

xpos = input("Start X Pos: ")
ypos = input("Start Y Pos: ")
degree = float(input("Angle (0 = up, clockwise): "))
length = float(input("Line Length: "))

xtwo = str(float(xpos) + (length * math.sin(math.radians(degree))))
ytwo = str(float(ypos) - (length * math.cos(math.radians(degree))))

print("l_at", xpos, ypos, xtwo, ytwo)
