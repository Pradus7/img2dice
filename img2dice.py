import sys, os
from PIL import Image
from math import ceil

DICE = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
count = {}


def img2dice(path, imgName, scale=1):
    """
    """
    #grayscale conversion
    img = Image.open(path + imgName).convert("L")

    #downscaling
    if scale > 1:
        img.thumbnail((img.width/scale, img.height/scale))

    #creating resulting text file
    result = open(f"result/{imgName}.txt", "w")

    for y in range(img.height):

        for x in range(img.width):
            #calculating which die to use for this pixel
            die = max(ceil(img.getpixel((x,y)) / 42.5), 1)
            count[die] = count.get(die, 0) + 1
            result.write(DICE[die-1])

        result.write("\n")

    result.write("\n")

    #Adding dice count at the end of the text file
    for i in range(len(DICE)):
        result.write(f"{i+1} dice appeared {count[i+1]} times.\n")

    result.close()


def main():
    filename = sys.argv[1]
    scale = 16
    if len(sys.argv) > 2:
        scale = int(float(sys.argv[2]))

    if os.path.isdir(filename):
        path = filename + '/'
        dirs = os.listdir(path)
        for item in dirs:
            if item.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                img2dice(path, item, scale)

    elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        img2dice("", filename, scale)


if __name__ == "__main__":
    main()