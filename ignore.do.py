import random

boardlist = ["         # ###         # # #         ### #        "]
allwords = {}
chosenboard = boardlist[random.randint(0,len(boardlist)-1)]
progressboard = list(chosenboard)
numberboard = progressboard
width = len(chosenboard)^0.5
def numbering():
    numberid = 1
    for y in range(width):
        for x in range(width):
            add = False
            base_value = chosenboard[y * width + x]
            if base_value == " ":
                for word in allwords:
                    worddata = allwords[word]
                    if worddata[4] == False:
                        if worddata[0] == "A" and worddata[2] == x:
                            allwords[word][1] += 1
                        elif worddata[0] == "D" and worddata[3] == y:
                            allwords[word][1] += 1
                        else:
                            allwords[word][4] = True
                if not x == width - 1:
                    if (chosenboard[y * width + x - 1] == "#" or x == 0) and chosenboard[y * width + x + 1] == " ":
                        add = True
                        numberboard[y * width + x] = numberid
                        allwords[str(numberid) + "A"] = ["A", 1, x, y, False]
                if not y == width - 1:
                    if (chosenboard[(y - 1) * width + x] == "#" or y == 0) and chosenboard[(y + 1) * width + x] == " ":
                        add = True
                        numberboard[y * width + x] = numberid
                        allwords[str(numberid) + "D"] = ["D", 1, x, y, False]
            if add:
                numberid += 1


def display_text_image():
    numberid = 0
    for times in range(2):
        row = "##"
        for x in range(width):
            row += "#"
        print(row)
    for y in range(width):
        for layer in range(2):
            row = "##"
            for x in range(width):
                pixel_value = progressboard[y * width + x]
                char = "##" if pixel_value == "#" else "  " if pixel_value == " " else " " + pixel_value
                row += char
            row += "##"
            print(row)
    row = "##"
    for x in range(width):
        row += "#"
    print(row)

def main():
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))
    
    pixel_data = []
    for _ in range(width * height):
        pixel_value = int(input("Enter pixel value (0 for black, 1 for white): "))
        pixel_data.append(pixel_value)
    print(pixel_data)
    
    display_text_image()

if __name__ == "__main__":
    main()