img2dice
=======

This python program converts images into an ascii art made up of dices.

Accomplished through the use of PIL.

⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅

Usage:
------

`python img2dice.py <directory/filename> <integer downscale factor>`

This program accepts both image files and directories that contain image files.

If given a directory, it will batch convert all image files within the directory.

The ingeger downscale factor is the ratio of pixel:dice, if no input is given the default value of 4 will be used to
generate an ascii art with ratio of 4 pixels to 1 dice.

Users can input a downscale factor of 1 if you desire a 1 pixel to 1 dice conversion ratio (it's gonna be a ton of dices).

After conversion, a `result` directory will be created and all converted ascii arts are stored in that directory with names `<filename>.txt`

Example:
------
![dog.jpg](example/dog.jpg)

`python img2dice.py dog.jpg`

[Result](https://htmlpreview.github.io/?https://github.com/Pradus7/img2dice/blob/master/example/example.html)
(Recommend viewing on desktop and zooming out)

Dices used:
1 dice appeared 14720 times.
2 dice appeared 14150 times.
3 dice appeared 24669 times.
4 dice appeared 13588 times.
5 dice appeared 6697 times.
6 dice appeared 9426 times.

Current features:
------
- Converts an image into an ascii art made up of dices 1:1 resolution (dice:pixel)
- Saves ascii art into a .txt file
- Ability to select custom downscaled resolutions: 1:2, 1:3, etc. (dice:pixel)
- Counts the amount of 1-6 dice used to make the image and places it at the end of the generated text file
- Ability to batch convert images placed inside a directory

