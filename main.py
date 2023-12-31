import tkinter as tk
from tkinter import StringVar
import random

#create object
root = tk.Tk()
root.title('Guess the Capital')
root.geometry("1000x1000")


#create a list to store user answers
user_answers = []

def user_input():
    global age_label, my_box, quiz_button
    my_text.destroy()
    start_button.destroy() 
    start_image_label.destroy()

    def number():
        try:
            age = int(my_box.get())
            if 10<= age <= 18:
                user_answers.config(text="")
                start_page()
            else:
                user_answers.config(text="Player must be between the age of 10 and 18!", fg="red", bg="#21243B")

        except ValueError:
            user_answers.config(text="Please enter a number!", fg="red", bg="#21243B")



    #colour of background
    root.configure(bg='#21243B')

    #enter your age label
    age_label = tk.Label(root, text="Enter your Age", font=("Verdana", 20), fg="white", bg='#21243B')
    age_label.pack(pady=20)

    my_box = tk.Entry(root)
    my_box.pack(pady=10)

    quiz_button = tk.Button(root, text="Start Quiz", command=number,font=("Verdana", 20), bg='#21243B')
    quiz_button.pack(pady=5)

    user_answers = tk.Label(root, text="", bg='#21243B')
    user_answers.pack(pady=20)



def start_page():
    global my_text, start_button, start_image, start_image_label

    # Load and display the background image
    start_image = tk.PhotoImage(file="image.png")
    start_image_label = tk.Label(root, image=start_image)
    start_image_label.image = start_image  # Keep a reference to the image
    start_image_label.place(x=0, y=0, relwidth=1, relheight=1)

    my_text = tk.Label(root, text="Guess The Capital", font=("Verdana", 50), fg="white", bg='#21243B')
    my_text.place(relx=0.5, rely=0.1, anchor="center")

    #Add start button
    start_button = tk.Button(root, text="Start", bg="#21243B", font=('Verdana', 20), padx=50, pady=10, command=question_Page)
    start_button.pack(pady=150)
        

def question_Page():
    my_box.destroy()
    age_label.destroy()
    quiz_button.destroy()
    my_text.destroy()
    start_button.destroy()
    start_image_label.destroy()

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
    
    #Store correct answers they are arranged in
    correct_answers = ['Tokyo', 'Paris', 'Madrid', 'Seoul', 'Beijing']

    #Shuffle questions, options ans corret_answers together
    shuffled_data = list(zip(questions, options, correct_answers))
    random.shuffle(shuffled_data)
    questions, options, correct_answers = zip(*shuffled_data)

    frame = tk.Frame(root, padx=10, pady=10, bg='#212435')
    question_label = tk.Label(frame, height=5, width=40, bg='#21243B', fg='#fff', font=('Verdana', 35), wraplength=500)
    
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

    #create a function to disable answer buttons
    def disableButtons(state):
        option1['state'] = state
        option2['state'] = state
        option3['state'] = state      
        option4['state'] = state 

    #create a function to check the selected answer

    def checkAnswer(radio):
        global correct, index

        user_answer =radio['text']#get the selected answer
        user_answers.append(user_answer)

        if user_answer == correct_answers[index]:
            correct +=1
            radio.config(bg='green')
        else:
            radio.config(bg='red')

        index +=1
        disableButtons('disable')

    #function to destory end page widgets 
    def destroy_end_page():
        end_frame.destroy()
        button_play_again.destroy()
        button_quit.destroy()
        end_image_label.destroy()
        score_label.destroy()
        

    #Creating my end page
    def end_page(score, total_questions):
        global end_frame, button_play_again, button_quit, end_image_label, score_label
        frame.destroy()

        #destroy any existing end page widgets
        if 'end_frame' in globals():
            destroy_end_page()

        #create an end page frame
        end_frame = tk.Frame(root, padx=10, pady=200, bg='#21243B')

        end_image = tk.PhotoImage(file="endpage.png")
        end_image_label = tk.Label(root, image=end_image)
        end_image_label.image = end_image  # Keep a reference to the image
        end_image_label.place(x=0, y=4, relwidth=1, relheight=1)

        score_label = tk.Label(root, text=f" {score}/{total_questions}", fg='#21243B', bg='white', font=('Verdana', 40))

        #pack widgets
        score_label.pack(pady=200)
        end_frame.pack(fill="both", expand="true")

        
        button_play_again = tk.Button(root, text="Play Again", command=restart_quiz, font=('Verdana', 20))
        button_quit = tk.Button(root, text="Exit", command=root.quit, font=('Verdana', 20), padx=35)

        #place the buttons below score 
        button_play_again.place(relx=0.5, rely=0.5, anchor="center", y=20)
        button_quit.place(relx=0.5, rely=0.5, anchor="center", y=60)

    def restart_quiz():
        global index, correct

        # Destroy end page widgets
        if 'end_frame' in globals():
            destroy_end_page()

        #reset variables
        index=0
        correct=0

        question_Page()


    # create a function to display the next question
    def displayNextQuestion():
        global index, correct

        #reset colour of all radiobuttons
        option1.config(bg='#21243B')
        option2.config(bg='#21243B')
        option3.config(bg='#21243B')
        option4.config(bg='#21243B')

        if button_next['text'] == 'Restart The Quiz':
            correct = 0
            index = 0
            question_label['bg'] = '#21243B'
            button_next['text'] = 'Next'     

        if index == len(options):
            end_page(correct, len(options))
            return
            

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

index = 0
correct = 0
start_page()

user_input()

#execute tkinter
root.mainloop()