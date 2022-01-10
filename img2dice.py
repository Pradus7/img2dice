from PIL import Image
from math import ceil

DICE = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
count = {}

def img2dice(imgPath, scale=1):
    """
    """
    img = Image.open(imgPath).convert("L")

    if scale > 1:
        img.thumbnail((img.width/scale, img.height/scale))

    result = open("result/result.txt", "w")

    for y in range(img.height):

        for x in range(img.width):
            die = max(ceil(img.getpixel((x,y)) / 42.5), 1)
            count[die] = count.get(die, 0) + 1
            result.write(DICE[die-1])

        result.write("\n")

    result.write("\n")

    for i in range(6):
        result.write(f"{i+1} dice appeared {count[i+1]} times.\n")

    result.close()

if __name__ == "__main__":
    img2dice("images/dog.jpg")