# img2dice
This is a program that converts an image placed inside the place_img_here folder into an image made up of dices through the use of PIL

&#2680; &#2681; &#2682; &#2683; &#2684; &#2685;

Usage:
`python img2dice.txt [directory/filename] [integer downscale factor, default=16]`

# Current features:
- Converts an image into a image made up of dices 1:1 resolution (dice:pixel)
- Saves converted image(s) into a .txt file
- Ability to select custom downscaled resolutions: 1:2, 1:3, etc. (dice:pixel)
- Counts the amount of 1-6 dice used to make the image and places it at the end of the generated text file
- Ability to batch convert images placed inside a directory

