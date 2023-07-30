import tkinter as tk


#create object
root = tk.Tk()
root.title('Guess the Captial')
root.geometry("1000x1000")

#question page background colour
root.configure(bg="#21243B")


#initialise score
score=0

#function to update the score
def update_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
def tab1():
   
   
    def Question_Page():
        global score
        my_text.destroy()
        button1.destroy()
        label1.destroy()

        my_text2 = tk.Label(root, text="What is the Capital of Japan?", font=("Helvetica", 40), fg="white", bg='#21243B')
        my_text2.grid(row=0,column=0, columnspan=2, sticky="n", pady=30)

        answer1 = tk.Button(root, text="Tokyo", font=("Helvetica", 25), height=2, width=1, command=update_score)
        answer1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        answer2 = tk.Button(root, text="Kyoto", font=("Helvetica", 25), height=2, width=1)
        answer2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        answer3 = tk.Button(root, text="Hiroshima", font=("Helvetica", 25), height=2, width=1)
        answer3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        answer4 = tk.Button(root, text="Osaka", font=("Helvetica", 25), height=2, width=1)
        answer4.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        
        #score label
        score_label.config(text=f"Score: {score}")
        score_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        # Configuring rows and columns to resize properly
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(3, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        
            

    #Add start button
    button1 = tk.Button(root, text="Start", padx=50, pady=10, command=Question_Page)
    button1.pack(pady=200)
    
    
#define Image
bg = tk.PhotoImage(file="image.png")

# create a label
label1 = tk.Label(root, image=bg)
label1.place(x=0, y=4, relwidth=1, relheight=1)

#Add something to the top of our image
my_text = tk.Label(root, text="Guess The Captial", font=("Helvetica", 50), fg="white", bg='#21243B')
my_text.pack(pady=50)

#score label
score_label= tk.Label(root, text = "Score: 0", font=("Helvetica", 20), fg="white", bg='#21243B')

tab1()

#execute tkinter
root.mainloop()

