from tkinter import *
import tkinter as tk


#create object
root = Tk()
root.title('Guess the Captial')
root.geometry("1000x1000")

#define Image
bg = PhotoImage(file="image.png")

# create a label
my_label = Label(root, image=bg)
my_label.place(x=0, y=4, relwidth=1, relheight=1)

#Add something to the top of our image
my_text = Label(root, text="Guess The Captial", font=("Helvetica", 50), fg="white", bg='#21243B')
my_text.pack(pady=50)


#execute tkinter
root.mainloop()

