import tkinter as tk
from tkinter import StringVar


#create object
root = tk.Tk()
root.title('Guess the Captial')
root.geometry("1000x1000")



def start_page():
    def question_Page1():
        #global score
        my_text.destroy()
        button1.destroy()
        label1.destroy()

        #colour of background
        root.configure(bg='#21243B')

        #list of questions
        questions = ["What is the Capital of Japan?", "What is the Capital of France?",
                     "What is the Capital of Spain?","What is the Capital of Korea?",
                     "What is the Capital of China?",]
        #possible answers
        options = [['Osaka','Tokyo','Chiba','Kyoto','Tokyo'],['Paris','Venice','Marseille','Bordeaux','Paris'],
                   ['Valencia','Seville','Barcelona','Madrid','Madrid'],['Daegu','Busan','Seoul','Incheon','Seoul'],
                   ['Shanghai','Guangzhou','Nanjing','Beijing','Beijing',]]
        
        frame = tk.Frame(root, padx=10, pady=10, bg='#212435')
        question_label = tk.Label(frame, height=5, width=40, bg='#21243B', fg='#fff', font=('Verdana', 35), wraplength=500)
        question_label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        frame_option_style = {"width": 300, "height": 150,  "bg": "#21243B", "highlightbackground": "#F2CC0C", "highlightthickness": 2 }

        #create frames around each option
        frame_option1 = tk.Frame(frame, **frame_option_style)
        frame_option2 = tk.Frame(frame, **frame_option_style)
        frame_option3 = tk.Frame(frame, **frame_option_style)
        frame_option4 = tk.Frame(frame, **frame_option_style)


        #place the frames within the grid
        frame_option1.grid(row=2, column=0, padx=10, pady=30)
        frame_option2.grid(row=2, column=1, padx=10, pady=30)
        frame_option3.grid(row=3, column=0, padx=10, pady=30)
        frame_option4.grid(row=3, column=1, padx=10, pady=30)

        #variables
        v1 = StringVar(frame)
        v2 = StringVar(frame)
        v3 = StringVar(frame)
        v4 = StringVar(frame)

        #answer buttons
        option1 = tk.Radiobutton(frame_option1, bg="#21243B", variable=v1, font=('Verdana', 25),
                                command = lambda : checkAnswer(option1))
        option2 = tk.Radiobutton(frame_option2, bg="#21243B", variable=v2, font=('Verdana', 25), 
                                command = lambda : checkAnswer(option2))
        option3 = tk.Radiobutton(frame_option3, bg="#21243B", variable=v3, font=('Verdana', 25), 
                                command = lambda : checkAnswer(option3))
        option4 = tk.Radiobutton(frame_option4, bg="#21243B", variable=v4, font=('Verdana', 25), 
                                command = lambda : checkAnswer(option4))
        
        #next button
        button_next = tk.Button(frame, text='Next', bg='#21243B', font=('Verdana', 20),
                                command = lambda : displayNextQuestion())
        
        frame.pack(fill="both", expand="true")
        question_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        
        #positioning the answer buttons
        option1.pack( padx=10, pady=10)
        option2.pack( padx=10, pady=10)
        option3.pack( padx=10, pady=10)
        option4.pack( padx=10, pady=10)


        #positioning the next button
        button_next.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

        index = 0
        correct = 0

        #create a function to disable answer buttons
        def disableButtons(state):
            option1['state'] = state
            option2['state'] = state
            option3['state'] = state      
            option4['state'] = state 

        #create a function to check the selected answer
        def checkAnswer(button):
            global correct, index

            if button['text'] == options[index][4]:
                correct +=1

            index +=1
            disableButtons('disable')

        # create a function to display the next question
        def displayNextQuestion():
            global index, correct

            if button_next['text'] == 'Restart The Quiz':
                correct = 0
                index = 0
                question_label['bg'] = '#21243B'
                button_next['text'] = 'Next'     

            if index == len(options):
                question_label['text'] = str(correct) + " / " + str(len(options))
                button_next['text'] = 'Restart The Quiz'
                if correct >= len(options)/2:
                    question_label['bg'] = 'green'
                else:
                    question_label['bg'] = 'red'

            else:
                question_label['text'] = questions[index]

                disableButtons('normal')
                opts = options[index]
                option1['text'] = opts[0]
                option2['text'] = opts[1]
                option3['text'] = opts[2]
                option4['text'] = opts[3]
                v1.set(opts[0])
                v2.set(opts[1])
                v3.set(opts[2])
                v4.set(opts[3])

                if index == len(options) - 1:
                    button_next['text'] = 'Check the Results'

        displayNextQuestion()



    #Add start button
    button1 = tk.Button(root, text="Start", font=('Verdana', 20), padx=50, pady=10, command=question_Page1)
    button1.pack(pady=200)
    
    
#define Image
bg = tk.PhotoImage(file="image.png")

# create a label
label1 = tk.Label(root, image=bg)
label1.place(x=0, y=4, relwidth=1, relheight=1)

#Add something to the top of our image
my_text = tk.Label(root, text="Guess The Captial", font=("Helvetica", 50), fg="white", bg='#21243B')
my_text.pack(pady=50)


index = 0
correct = 0
start_page()


#execute tkinter
root.mainloop()

