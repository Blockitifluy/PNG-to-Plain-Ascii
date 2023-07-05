# PNG-to-Ascii-Art
 
This is PNG to Ascii Art. It job is to convert a PNG to a txt file full of Ascii Art.  Eg. Lets have an example of a cat (_Cat Test.png_); Here is a result - **Brightness** of 1, **Size** of 50 characters:

The Orignal Image         |  The Resulted Image
:-------------------------:|:-------------------------:
![](./Examples/Cat%20Test.png)   |  ![](./Examples/Cat%20PNG%20Result.png)

# How does it Works? #

* First, it transforms the image to grayscale, downscales it to the _size_ propetry and brightens it using the _brightness_ input.
* Then, plays a for loop, the character that appear which are based on The **Depth.txt** and the darkness of the pixel
* Finally prints it to the **result.txt** file

## Python Packages: ##

* PIL (The Image Reader)
* os _(Pre-installed)_
* tkinter **(For the UI)**

# How To Use #

To use the App, Open _AsciiArt.py_ **not** **_AsciiApp.py_** due to the fact it handles the UI, not the functionality of the script.

**Cat Image Examples from PNGWing [Here](https://www.pngwing.com/en/search?q=cat)**