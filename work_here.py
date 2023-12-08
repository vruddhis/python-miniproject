from tkinter import *
from tkinter import PhotoImage
import pandas as pd
import tkinter as tk
from tkinter.font import Font

class Question:
    def __init__(self, row):
        self.question_statement = row['Question']
        self.option1 = row['Option1']
        self.option2 = row['Option2']
        self.option3 = row['Option3']
        self.option4 = row['Option4']
        self.tinyscore = 0        
        self.correct_answer = row['Correct answer']

    def check1(self):
        if self.option1 == self.correct_answer:
            self.tinyscore = 1
            print(self.tinyscore)            
        else:
            self.tinyscore = 0
            print(self.tinyscore)  
            
    def check2(self):
        if self.option2 == self.correct_answer:
            self.tinyscore = 1
            print(self.tinyscore)  
        else:
            self.tinyscore = 0
            print(self.tinyscore)  
    def check3(self):
        if self.option3 == self.correct_answer:
            self.tinyscore = 1 
            print(self.tinyscore)             
        else:
            self.tinyscore = 0
            print(self.tinyscore)  
    def check4(self):
        if self.option4 == self.correct_answer:
            self.tinyscore = 1  
            print(self.tinyscore)            
        else:
            self.tinyscore = 0
            print(self.tinyscore)  
def selectq(subject):
    df = pd.read_csv("python_mini.csv")
    if subject == "all":
        subject_questions = df
    else:
        subject_questions = df[df['Subject'] == subject]
    selected_questions = subject_questions.sample(n=5)
    questions = []
    for index, row in selected_questions.iterrows():       
        question = Question(row)
        questions.append(question)
    return questions

root = tk.Tk()
welcome_font=Font(family="Times",size=50,weight="bold")
button_font=Font(family="Helvetica",size=18)
wc_option_font=Font(family="Helvetica",size=13)
q_font=Font(family="Helvetica",size=24)
root.configure(bg="white")

# mathbg=PhotoImage(file="mathbg.png")
# mathbgimg=tk.PhotoImage(mathbg)
# mathbg_label = tk.Label(root, image=mathbgimg)
# mathbg_label.place(x=0, y=0, relwidth=1, relheight=1)

# mathbg_label.image=mathbgimg

bg=PhotoImage(file="q_n_excl.png")
startquizimg=bg.subsample(10)

globe=PhotoImage(file="globe.png")
globeimg=globe.subsample(10)

calc=PhotoImage(file="calc.png")
calcimg=calc.subsample(10)

dna=PhotoImage(file="dna.png")
dnaimg=dna.subsample(10)

surp=PhotoImage(file="surp.png")
surpriseme=surp.subsample(10)

star=PhotoImage(file="star.png")
starimg=star.subsample(11)

feather=PhotoImage(file="feather.png")
feathimg=feather.subsample(10)


class quiz:
    def __init__(self, root):
        self.score = 0
        self.subject = "all"
        self.x = True
        self.questions = []
        self.question_window1 = root
        self.question_window1.title("Quiz")
        self.widgets = []
        self.theme = "Any"
        self.welcomescreen()

    def xyz(self): 
        self.startquiz(self.subject)

    def displayquestion1(self):
        for i in self.widgets:
            i.destroy()
        self.question_window1.configure(bg="white")

        question_label = tk.Label(self.question_window1, text=self.questions[0].question_statement, font=q_font, bg="white")
        question_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        option1_button = tk.Button(self.question_window1, text=self.questions[0].option1, command=self.questions[0].check1, font=button_font, bg="white")
        option1_button.place(relx=0.25, rely=0.4, anchor=CENTER) 
        option2_button = tk.Button(self.question_window1, text=self.questions[0].option2, command=self.questions[0].check2, font=button_font, bg="white")
        option2_button.place(relx=0.75, rely=0.4, anchor=CENTER)

        option3_button = tk.Button(self.question_window1, text=self.questions[0].option3, command=self.questions[0].check3, font=button_font, bg="white")
        option3_button.place(relx=0.25, rely=0.6, anchor=CENTER)
        option4_button = tk.Button(self.question_window1, text=self.questions[0].option4, command=self.questions[0].check4, font=button_font, bg="white")
        option4_button.place(relx=0.75, rely=0.6, anchor=CENTER)

        next_button = tk.Button(self.question_window1, text="Next", command=self.displayquestion2, font=button_font, bg="white")
        next_button.place(relx=0.5, rely=0.8, anchor=CENTER)  

        self.widgets = [question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    def displayquestion2(self):
        for i in self.widgets:
            i.destroy()
        self.question_window1.configure(bg="white")

        question_label = tk.Label(self.question_window1, text=self.questions[1].question_statement, font=q_font, bg="white")
        question_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        option1_button = tk.Button(self.question_window1, text=self.questions[1].option1, command=self.questions[1].check1, font=button_font, bg="white")
        option1_button.place(relx=0.25, rely=0.4, anchor=CENTER)
        option2_button = tk.Button(self.question_window1, text=self.questions[1].option2, command=self.questions[1].check2, font=button_font, bg="white")
        option2_button.place(relx=0.75, rely=0.4, anchor=CENTER)

        option3_button = tk.Button(self.question_window1, text=self.questions[1].option3, command=self.questions[1].check3, font=button_font, bg="white")
        option3_button.place(relx=0.25, rely=0.6, anchor=CENTER)
        option4_button = tk.Button(self.question_window1, text=self.questions[1].option4, command=self.questions[1].check4, font=button_font, bg="white")
        option4_button.place(relx=0.75, rely=0.6, anchor=CENTER)

        previous_button = tk.Button(self.question_window1, text="Previous", command=self.displayquestion1, font=button_font, bg="white")
        previous_button.place(relx=0.35, rely=0.8, anchor=CENTER)
        next_button = tk.Button(self.question_window1, text="Next", command=self.displayquestion3, font=button_font, bg="white")
        next_button.place(relx=0.65, rely=0.8, anchor=CENTER)

        self.widgets = [question_label, option1_button, option2_button, option3_button, option4_button, previous_button, next_button]

    def displayquestion3(self):
        for i in self.widgets:
            i.destroy()
        self.question_window1.configure(bg="white")

        question_label = tk.Label(self.question_window1, text=self.questions[2].question_statement, font=q_font, bg="white")
        question_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        option1_button = tk.Button(self.question_window1, text=self.questions[2].option1, command=self.questions[2].check1, font=button_font, bg="white")
        option1_button.place(relx=0.25, rely=0.4, anchor=CENTER)
        option2_button = tk.Button(self.question_window1, text=self.questions[2].option2, command=self.questions[2].check2, font=button_font, bg="white")
        option2_button.place(relx=0.75, rely=0.4, anchor=CENTER)

        option3_button = tk.Button(self.question_window1, text=self.questions[2].option3, command=self.questions[2].check3, font=button_font, bg="white")
        option3_button.place(relx=0.25, rely=0.6, anchor=CENTER)
        option4_button = tk.Button(self.question_window1, text=self.questions[2].option4, command=self.questions[2].check4, font=button_font, bg="white")
        option4_button.place(relx=0.75, rely=0.6, anchor=CENTER)

        previous_button = tk.Button(self.question_window1, text="Previous", command=self.displayquestion2, font=button_font, bg="white")
        previous_button.place(relx=0.35, rely=0.8, anchor=CENTER)
        next_button = tk.Button(self.question_window1, text="Next", command=self.displayquestion4, font=button_font, bg="white")
        next_button.place(relx=0.65, rely=0.8, anchor=CENTER)

        self.widgets = [question_label, option1_button, option2_button, option3_button, option4_button, previous_button, next_button]

    def displayquestion4(self):
        for i in self.widgets:
            i.destroy()
        self.question_window1.configure(bg="white")

        question_label = tk.Label(self.question_window1, text=self.questions[3].question_statement, font=q_font, bg="white")
        question_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        option1_button = tk.Button(self.question_window1, text=self.questions[3].option1, command=self.questions[3].check1, font=button_font, bg="white")
        option1_button.place(relx=0.25, rely=0.4, anchor=CENTER)
        option2_button = tk.Button(self.question_window1, text=self.questions[3].option2, command=self.questions[3].check2, font=button_font, bg="white")
        option2_button.place(relx=0.75, rely=0.4, anchor=CENTER)

        option3_button = tk.Button(self.question_window1, text=self.questions[3].option3, command=self.questions[3].check3, font=button_font, bg="white")
        option3_button.place(relx=0.25, rely=0.6, anchor=CENTER)
        option4_button = tk.Button(self.question_window1, text=self.questions[3].option4, command=self.questions[3].check4, font=button_font, bg="white")
        option4_button.place(relx=0.75, rely=0.6, anchor=CENTER)

        previous_button = tk.Button(self.question_window1, text="Previous", command=self.displayquestion3, font=button_font, bg="white")
        previous_button.place(relx=0.35, rely=0.8, anchor=CENTER)
        next_button = tk.Button(self.question_window1, text="Next", command=self.displayquestion5, font=button_font, bg="white")
        next_button.place(relx=0.65, rely=0.8, anchor=CENTER)

        self.widgets = [question_label, option1_button, option2_button, option3_button, option4_button, previous_button, next_button]

    def displayquestion5(self):
        for i in self.widgets:
            i.destroy()
        self.question_window1.configure(bg="white")

        question_label = tk.Label(self.question_window1, text=self.questions[4].question_statement, font=q_font, bg="white")
        question_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        option1_button = tk.Button(self.question_window1, text=self.questions[4].option1, command=self.questions[4].check1, font=button_font, bg="white")
        option1_button.place(relx=0.25, rely=0.4, anchor=CENTER)
        option2_button = tk.Button(self.question_window1, text=self.questions[4].option2, command=self.questions[4].check2, font=button_font, bg="white")
        option2_button.place(relx=0.75, rely=0.4, anchor=CENTER)

        option3_button = tk.Button(self.question_window1, text=self.questions[4].option3, command=self.questions[4].check3, font=button_font, bg="white")
        option3_button.place(relx=0.25, rely=0.6, anchor=CENTER)
        option4_button = tk.Button(self.question_window1, text=self.questions[4].option4, command=self.questions[4].check4, font=button_font, bg="white")
        option4_button.place(relx=0.75, rely=0.6, anchor=CENTER)

        previous_button = tk.Button(self.question_window1, text="Previous", command=self.displayquestion4, font=button_font, bg="white")
        previous_button.place(relx=0.35, rely=0.8, anchor=CENTER)
        end_button = tk.Button(self.question_window1, text="End Quiz", command=self.show_score, font=button_font, bg="white")
        end_button.place(relx=0.65, rely=0.8, anchor=CENTER)

        self.widgets = [question_label, option1_button, option2_button, option3_button, option4_button, previous_button, end_button]

    def startquiz(self, sub):
        self.questions = selectq(sub)
        self.displayquestion1()        
    def setmaths(self):
        self.subject = "Maths"
    def setscience(self):
        self.subject = "Science"      
    def sethistory(self):
        self.subject = "History"
    def setgeo(self):
        self.subject = "Geography"
    def setastro(self):
        self.subject = "Astronomy"
        
    def welcomescreen(self):
        width= self.question_window1.winfo_screenwidth() 
        height= self.question_window1.winfo_screenheight()
        self.question_window1.geometry("%dx%d" % (width, height))
        self.question_window1.configure(bg="white")

        welcome_font = Font(family="times new roman", size=50, weight="bold")
        button_font = Font(family="Roboto", size=18)
        wc_option_font = Font(family="Roboto", size=13)
        select_sub_font=Font(family="Roboto",size=15)

        text = "Instructions:\n1. Click 'Start Quiz' to begin.\n2. Select a subject or choose 'Surprise me' for random questions.\n3. Answer each question by clicking the appropriate option.\nNote: Only your last selected option will be considered.\n4. Click 'Next' to move to the next question, 'Previous' to move to the previous one and 'End Quiz' to finish."

        instructions_label = tk.Label(self.question_window1, text=text, bg="white", font=button_font)
        instructions_label.place(relx=0.5, rely=0.3, anchor="center")

        welcome_label = tk.Label(self.question_window1, text="Welcome to the QuizLand", bg="white", font=welcome_font)
        welcome_label.place(relx=0.5, rely=0.1, anchor="center")

        start = tk.Button(self.question_window1, text="Start quiz", command=self.xyz, bg="white", font=wc_option_font,image=startquizimg,compound=LEFT)
        start.place(relx=0.5, rely=0.8, anchor="center")

        subject_label = tk.Label(self.question_window1, text="Select Subject:", bg="white", font=select_sub_font)
        subject_label.place(relx=0.5, rely=0.5, anchor="center")

        all_button = tk.Button(self.question_window1, text="Surprise me!", bg="white", font=wc_option_font,image=surpriseme,compound=LEFT)
        all_button.place(relx=0.3, rely=0.6, anchor="center")

        maths_button = tk.Button(self.question_window1, text="Mathematics", bg="white", command=self.setmaths, font=wc_option_font,image=calcimg,compound=LEFT)
        maths_button.place(relx=0.5, rely=0.6, anchor="center")

        science_button = tk.Button(self.question_window1, text="Science", bg="white", command=self.setscience, font=wc_option_font,image=dnaimg,compound=LEFT)
        science_button.place(relx=0.7, rely=0.6, anchor="center")

        history_button = tk.Button(self.question_window1, text="History", bg="white", command=self.sethistory, font=wc_option_font,image=feathimg,compound=LEFT)
        history_button.place(relx=0.3, rely=0.7, anchor="center")

        geo_button = tk.Button(self.question_window1, text="Geography", bg="white", command=self.setgeo, font=wc_option_font,image=globeimg,compound=LEFT)
        geo_button.place(relx=0.5, rely=0.7, anchor="center")

        astro_button = tk.Button(self.question_window1, text="Astronomy", bg="white", command=self.setastro, font=wc_option_font,image=starimg,compound=LEFT)
        astro_button.place(relx=0.7, rely=0.7, anchor="center")

        self.widgets = [
            instructions_label, welcome_label, start, subject_label, all_button,
            maths_button, science_button, history_button, geo_button, astro_button
        ]

    def show_score(self):
        for i in self.widgets:
            i.destroy()
        for i in self.questions:
            self.score += i.tinyscore
        score_message = f"Your Final Score: {self.score}/5"
        score_label=tk.Label(self.question_window1,text=score_message,bg="white",font=button_font)
        score_label.pack()

swhoo=quiz(root)
root.mainloop()
