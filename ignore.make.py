def display_text_image(pixel_data, width, height):
    row = ""
    for y in range(height):
        for x in range(width):
            pixel_value = pixel_data[y * width + x]
            char = "#" if pixel_value == 0 else " "
            row += char
    print("\"" + row + "\"")
#"         # ###         # # #         ### #        "
def main():
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))
    
    pixel_data = []
    for _ in range(width * height):
        pixel_value = int(input("Enter pixel value (0 for black, 1 for white): "))
        pixel_data.append(pixel_value)
    print(pixel_data)
    
    display_text_image(pixel_data, width, height)

if __name__ == "__main__":
    main()