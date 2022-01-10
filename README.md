img2dice
=======

This program converts images into an ascii art made up of dices.

Accomplished through the use of PIL.

⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅

Usage:
------

`python img2dice.txt [directory/filename] [integer downscale factor, default=4]`

The converted text files will be placed in the `result` directory and all files will be named `<filename>.txt`.

Example:
------
![](images/cat.jpg)

`python img2dice.txt cat.jpg`

[result](example.html)

Current features:
------
- Converts an image into a image made up of dices 1:1 resolution (dice:pixel)
- Saves converted image(s) into a .txt file
- Ability to select custom downscaled resolutions: 1:2, 1:3, etc. (dice:pixel)
- Counts the amount of 1-6 dice used to make the image and places it at the end of the generated text file
- Ability to batch convert images placed inside a directory

