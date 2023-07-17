from tkinter import *
import tkinter as tk

#create object
master = tk.Tk()




#add image file
bgimg = tk.PhotoImage(file= "image.png")


limg= Label(master, i=bgimg)
limg.pack()

#execute tkinter
master.mainloop()

