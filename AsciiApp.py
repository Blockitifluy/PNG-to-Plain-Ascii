import tkinter as tk

FONT_FAMILY = 'Segoe UI Variable'

class root:
    elements = {}

    def __init__(self, onSubmit, getFile):
        self.root = tk.Tk()

        self.root.geometry("350x250")
        self.root.title("PNG to Txt")

        #Row 0
        sizeLabel = tk.Label(self.root, height=1, text="Size: ", font=(FONT_FAMILY, 10))
        sizeLabel.grid(row=0,column=0, padx=10, pady=10)

        sizeInput = tk.Entry(self.root, font=(FONT_FAMILY, 16))
        print(sizeInput.get())
        sizeInput.grid(padx=10, pady=10, column=1, row=0)
        self.elements["SizeInput"] = sizeInput

        #Row 1
        brightLabel = tk.Label(self.root, height=1, text="Brightness: ", font=(FONT_FAMILY, 10))
        brightLabel.grid(padx=0, pady=10, column=0, row=1)

        brightInput = tk.Entry(self.root, font=(FONT_FAMILY, 16))
        brightInput.grid(padx=0, pady=10, column=1, row=1)
        self.elements["BrightInput"] = brightInput

        #Row 2
        fileButton = tk.Button(self.root, height=1, text="Get File", font=(FONT_FAMILY, 12), command=getFile)
        fileButton.grid(padx=0, pady=10, column=1, row=2)

        fileDir = tk.Label(self.root, height=1, font=(FONT_FAMILY, 8), text="")
        fileDir.grid(padx=0,pady=10,column=0,row=2)
        self.elements["FileDir"] = fileDir

        #Row 3
        subResult = tk.Label(self.root, height=1, font=(FONT_FAMILY, 12))
        subResult.grid(padx=10, pady=10, column=0, row=3)
        self.elements["SubResult"] = subResult

        submit = tk.Button(self.root, font=(FONT_FAMILY, 12), height=1, text="Submit", command=onSubmit)
        submit.grid(padx=10, pady=10, column=1, row=3)