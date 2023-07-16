import tkinter 
from tkinter import *

root = tkinter.Tk()

root.geometry("1000x900")
root.title("Guess the Capital")
root.config(background="#21243B")
img1 = PhotoImage(file="Untitled design-PhotoRoom.png-PhotoRoom.png")


labelimage = Label(
    root,
    image = img1,
    background = "#21243B"
)
labelimage.pack()

labeltext = Label(
    root,
    text = "Guess the Captial",
    font = ("Arial", 24, "bold")
)
labeltext.pack()
root.mainloop()

