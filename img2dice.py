from PIL import Image
from math import ceil

DICE = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

def img2dice(imgPath, scale=1):
    img = Image.open(imgPath).convert("L")
    if scale > 1:
        img.thumbnail((img.width/scale, img.height/scale))
    canvas = open("result/result.txt", "w")
    for y in range(img.height):
        for x in range(img.width):
            canvas.write(DICE[ceil(img.getpixel((x,y)) / 42.5)-1])
        canvas.write("\n")
    canvas.close()

if __name__ == "__main__":
    img2dice("images/dog.jpg")