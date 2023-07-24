import tkinter as tk


#create object
root = tk.Tk()
root.title('Guess the Captial')
root.geometry("1000x1000")

#define Image
bg = tk.PhotoImage(file="image.png")

# create a label
label1 = tk.Label(root, image=bg)
label1.place(x=0, y=4, relwidth=1, relheight=1)

#Add something to the top of our image
my_text = tk.Label(root, text="Guess The Captial", font=("Helvetica", 50), fg="white", bg='#21243B')
my_text.pack(pady=50)

#Add start button
button1 = tk.Button(root, text="Start", padx=50, pady=10)
button1.pack(pady=200)


#execute tkinter
root.mainloop()

