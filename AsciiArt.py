from PIL import Image, ImageEnhance
from tkinter import filedialog

from os import path as osPath

import AsciiApp as PNGApp

CurrentImage = None

ImageDirectory = "Cat Test.png"
ImageSize = 100

DepthFile = open('Depth.txt',"r").read().split()

DepthList = []

def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default

def DictToArray(Dict):
    result = []

    for x in Dict:
        result.append(x)

    return result
    
def ReformatDepthFile():
    maxValue = 255

    dMargin = maxValue // len(DepthFile)

    reform = {}

    for i, char in enumerate(DepthFile):
        reform[str(i * dMargin)] = char

    for rgbRange in range(0, maxValue):
        closest = " "

        for d in reform:
            char = reform[str(d)]
            
            if int(d) > rgbRange:
                closest = char
                break

        DepthList.append(closest)
        
ReformatDepthFile()

def FilePop():
    global ImageDirectory

    NewFile = filedialog.askopenfilename()

    ImageDirectory = NewFile

    FileName = osPath.basename(ImageDirectory)
    
    print(NewFile, FileName)

    APP.elements["FileDir"].config(text = FileName)

def pixelLoop():
    lines = ""

    for y in range(ImageSize[0]):
        lineR = "\n"

        for x in range(ImageSize[1]):
            try:
                color = CurrentImage.getpixel((x, y))
            except IndexError:
                color = -1
            
            char = safe_list_get(DepthList, color, " ") + " "

            lineR += char

        lines += lineR

    return lines

def getRatioOfImage(Image):
    size = Image.size
    
    ratio = size[0] / size[1]
    print(f"The image ratio is {ratio}")
    return ratio

def startup():
    global ImageDirectory, ImageSize, CurrentImage, MaxSize

    MaxSize_a = float(APP.elements["SizeInput"].get())
    Brightness = 1 / float( APP.elements["BrightInput"].get())

    try:
        CurrentImage = Image.open(ImageDirectory).convert('L')

        MaxSize = (int(MaxSize_a * getRatioOfImage(CurrentImage)) , int(MaxSize_a))
        
        CurrentImage.thumbnail(MaxSize)
        print(f"Max Size is {MaxSize}, The Current Size is {CurrentImage.size}")
        ImageSize = MaxSize

        brightEnhance = ImageEnhance.Brightness(CurrentImage)
        CurrentImage = brightEnhance.enhance(Brightness)

        textfile = pixelLoop()

        resultFile = open("result.txt","w")
        resultFile.write(textfile)
        resultFile.close()

        CurrentImage.close()

        APP.elements["SubResult"].config(text="Successfully Made File")
    except FileNotFoundError:
        print("File Not Found")

        APP.elements["SubResult"].config(text="Error: File Not Found")

APP = PNGApp.root(startup, FilePop)

APP.root.mainloop()