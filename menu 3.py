"""
Program for GUI menu screen with buttons.
Next step is to introduce raised buttons and make them clickable.
Having trouble placing elements atop one another. elements like an image.
Not sure im importing the correct modules or class.

# Importing from tkinter 
from tkinter import *
# Creating a root window
root = Tk()
root.maxsize(600, 600)
root.config(bg="Grey")

class MainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.initUI()
# Creating buttons and background image
    def initUI(self):
        self.master.title("Menu Screen")
        bgImage = PhotoImage(file="Cave.gif")

        newButton = Button(self, text="New Game", height=2,width=20,
                               command=self.newGame)
        newButton.pack(side=TOP, pady=50)
        
        label = Label(self, image=bg)
        label.image = bgImage
        label.pack(fill=BOTH, expand=1)

        self.pack()
"""

# Edited 12/5/2024. Was trying to use PyQT5 instead of tkinter which caused
# program to fail. Learning PYQT5 on my own time , this assignment is for tkinter only.
# Original code above.

# Importing from tkinter
from tkinter import *
# Creating root window
root = Tk()
# Adjusting size and adding image. Not sure of resizing image
root.maxsize(706, 398)
bg = PhotoImage(file = "Cave.gif")
# Showing the image as a label , tkinter has no built in function for images as backgrounds 
bgImage = Label( root, image = bg)
bgImage.place(x = 0, y = 0)
# Creating frame and buttons
class MainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        newButton = Button(self, text="New Game", height=2, width=20,
                           command=self.newGame)
        newButton.pack(side=TOP, pady=50)

        label = Label(self, image=bg)
        label.image = bgImage
        label.pack(fill=BOTH, expand=1)

        self.pack()

root.mainloop()

