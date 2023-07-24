import tkinter as tk


#create object
root = tk.Tk()
root.title('Guess the Captial')
root.geometry("1000x1000")

#question page background colour
root.configure(bg="#21243B")

def tab1():
    def tab2():
        my_text.destroy()
        button1.destroy()
        label1.destroy()

        my_text2 = tk.Label(root, text="What is the Capital of Japan?", font=("Helvetica", 40), fg="white", bg='#21243B')
        my_text2.pack(pady=50)

    #Add start button
    button1 = tk.Button(root, text="Start", padx=50, pady=10, command=tab2)
    button1.pack(pady=200)
    
#define Image
bg = tk.PhotoImage(file="image.png")

# create a label
label1 = tk.Label(root, image=bg)
label1.place(x=0, y=4, relwidth=1, relheight=1)

#Add title
my_text = tk.Label(root, text="Guess The Captial", font=("Helvetica", 50), fg="white", bg='#21243B')
my_text.pack(pady=50)




tab1()

#execute tkinter
root.mainloop()

