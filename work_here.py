from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage, Canvas
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

bg=PhotoImage(file="q_n_excl.png")
startquizimg=bg.subsample(10)

globe=PhotoImage(file="globe.png")
globeimg=globe.subsample(10)

calc=PhotoImage(file="calc.png")
calcimg=calc.subsample(10)

dna=PhotoImage(file="dna.png")
dnaimg=dna.subsample(10)

star=PhotoImage(file="star.png")
starimg=star.subsample(11)

feather=PhotoImage(file="feather.png")
feathimg=feather.subsample(10)
# c1=Canvas(root)
# c1.grid(row=0,column=3)
# c1.create_image(0,0, image=bg,anchor="nw")


class quiz:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.root.title("Quiz")
        self.subject = "all"
        self.welcomescreen()
        self.x = True
        self.questions = []
        self.question_window1 = None
        self.widgets = []
        self.theme = "Any"

    def xyz(self): 
        self.startquiz(self.subject)

    def displayquestion1(self):
        self.question_window1 = tk.Toplevel(self.root)
        self.question_window1.configure(bg="white")
        width= self.question_window1.winfo_screenwidth() 
        height= self.question_window1.winfo_screenheight()
        self.question_window1.geometry("%dx%d" % (width, height))

        question_label = tk.Label(self.question_window1, text=self.questions[0].question_statement,font=q_font,bg="white")
        question_label.grid()

        option1_button = tk.Button(self.question_window1, text=self.questions[0].option1, command=self.questions[0].check1,font=button_font,bg="white")
        option1_button.grid()

        option2_button = tk.Button(self.question_window1, text=self.questions[0].option2, command=self.questions[0].check2,font=button_font,bg="white")
        option2_button.grid()

        option3_button = tk.Button(self.question_window1, text=self.questions[0].option3, command=self.questions[0].check3,font=button_font,bg="white")
        option3_button.grid()

        option4_button = tk.Button(self.question_window1, text=self.questions[0].option4, command=self.questions[0].check4,font=button_font,bg="white")
        option4_button.grid()

        next_button = tk.Button(self.question_window1, text = "Next", command = self.displayquestion2,font=button_font,bg="white")
        next_button.grid()

        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    def displayquestion2(self):
        for i in self.widgets:
            i.destroy()
        question_label = tk.Label(self.question_window1, text=self.questions[1].question_statement,font=q_font,bg="white")
        question_label.grid()

        option1_button = tk.Button(self.question_window1, text=self.questions[1].option1, command=self.questions[1].check1,font=button_font,bg="white")
        option1_button.grid()

        option2_button = tk.Button(self.question_window1, text=self.questions[1].option2, command=self.questions[1].check2,font=button_font,bg="white")
        option2_button.grid()

        option3_button = tk.Button(self.question_window1, text=self.questions[1].option3, command=self.questions[1].check3,font=button_font,bg="white")
        option3_button.grid()

        option4_button = tk.Button(self.question_window1, text=self.questions[1].option4, command=self.questions[1].check4,font=button_font,bg="white")
        option4_button.grid()

        previous_button = tk.Button(self.question_window1, text = "Previous", command = self.displayquestion1,font=button_font,bg="white")
        previous_button.grid()

        next_button = tk.Button(self.question_window1, text = "Next", command = self.displayquestion3,font=button_font,bg="white")
        next_button.grid()
        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    def displayquestion3(self):
        for i in self.widgets:
            i.destroy()

        question_label = tk.Label(self.question_window1, text=self.questions[2].question_statement,font=q_font,bg="white")
        question_label.grid()
        option1_button = tk.Button(self.question_window1, text=self.questions[2].option1, command=self.questions[2].check1,font=button_font,bg="white")
        option1_button.grid()

        option2_button = tk.Button(self.question_window1, text=self.questions[2].option2, command=self.questions[2].check2,font=button_font,bg="white")
        option2_button.grid()

        option3_button = tk.Button(self.question_window1, text=self.questions[2].option3, command=self.questions[2].check3,font=button_font,bg="white")
        option3_button.grid()

        option4_button = tk.Button(self.question_window1, text=self.questions[2].option4, command=self.questions[2].check4,font=button_font,bg="white")
        option4_button.grid()

        previous_button = tk.Button(self.question_window1, text = "Previous", command = self.displayquestion2,font=button_font,bg="white")
        previous_button.grid()

        next_button = tk.Button(self.question_window1, text = "Next", command = self.displayquestion4,font=button_font,bg="white")
        next_button.grid()
        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    def displayquestion4(self):
        for i in self.widgets:
            i.destroy()
        question_label = tk.Label(self.question_window1, text=self.questions[3].question_statement,font=q_font,bg="white")
        question_label.grid()

        option1_button = tk.Button(self.question_window1, text=self.questions[3].option1, command=self.questions[3].check1,font=button_font,bg="white")
        option1_button.grid()

        option2_button = tk.Button(self.question_window1, text=self.questions[3].option2, command=self.questions[3].check2,font=button_font,bg="white")
        option2_button.grid()

        option3_button = tk.Button(self.question_window1, text=self.questions[3].option3, command=self.questions[3].check3,font=button_font,bg="white")
        option3_button.grid()

        option4_button = tk.Button(self.question_window1, text=self.questions[3].option4, command=self.questions[3].check4,font=button_font,bg="white")
        option4_button.grid()

        previous_button = tk.Button(self.question_window1, text = "Previous", command = self.displayquestion3,font=button_font,bg="white")
        previous_button.grid()

        next_button = tk.Button(self.question_window1, text = "Next", command = self.displayquestion5,font=button_font,bg="white")
        next_button.grid()
        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    def displayquestion5(self):
        for i in self.widgets:
            i.destroy()
        question_label = tk.Label(self.question_window1, text=self.questions[4].question_statement,font=q_font,bg="white")
        question_label.grid()

        option1_button = tk.Button(self.question_window1, text=self.questions[4].option1, command=self.questions[4].check1,font=button_font,bg="white")
        option1_button.grid()

        option2_button = tk.Button(self.question_window1, text=self.questions[4].option2, command=self.questions[4].check2,font=button_font,bg="white")
        option2_button.grid()

        option3_button = tk.Button(self.question_window1, text=self.questions[4].option3, command=self.questions[4].check3,font=button_font,bg="white")
        option3_button.grid()

        option4_button = tk.Button(self.question_window1, text=self.questions[4].option4, command=self.questions[4].check4,font=button_font,bg="white")
        option4_button.grid()

        previous_button = tk.Button(self.question_window1, text = "Previous", command = self.displayquestion4,font=button_font,bg="white")
        previous_button.grid()

        next_button = tk.Button(self.question_window1, text = "End Quiz", command = self.show_score,font=button_font,bg="white")
        next_button.grid()
        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]
    
    def startquiz(self, sub):
        self.questions = selectq(sub)
        self.displayquestion1()
        
    def setmaths(self):
        self.subject = "Maths"
        self.theme = "Maths"

    def setscience(self):
        self.subject = "Science"
        

    def sethistory(self):
        self.subject = "History"
    def setgeo(self):
        self.subject = "Geography"
    def setastro(self):
        self.subject = "Astronomy"
        
    def welcomescreen(self):
        # bg=ImageTk.PhotoImage(file="question.png")
        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))

        root.title("Quiz Welcome!")

        text = "Instructions:\n1. Click 'Start Quiz' to begin.\n2. Select a subject or choose 'Any' for random questions.\n3. Answer each question by clicking the appropriate option. \nNote: Only your last selected option will be considered.\n4. Click 'Next' to move to the next question or 'End Quiz' to finish."
        instructions_label = tk.Label(self.root, text=text, bg="white",font=button_font)
        instructions_label.grid(row=3, column=1)

        welcome_label=tk.Label(self.root,text="Welcome to the QuizLand",bg="white",font=welcome_font)
        welcome_label.grid(row=1,column=1)

        start = tk.Button(text = "Start quiz",command = self.xyz,bg="white", font=wc_option_font,image=startquizimg,compound=LEFT)
        start.grid(row=17,column=1)
        space=tk.Label(text=" ",bg="white")
        space.grid(row=15,column=1)
        space2=tk.Label(text=" ",bg="white")
        space2.grid(row=16,column=1)
        space3=tk.Label(text=" ",bg="white")
        space3.grid(row=4,column=1)
        subject_label = tk.Label(self.root, text="Select Subject:",bg="white",font=wc_option_font)
        subject_label.grid(row=6,column=1)
        space4=tk.Label(text=" ",bg="white")
        space4.grid(row=7,column=1)
        all_button = tk.Button(self.root, text = "Any",bg="white", font=wc_option_font)
        all_button.grid(row=9,column=1)
        maths_button = tk.Button(self.root, text = "Mathematics",bg="white", command = self.setmaths, font=wc_option_font,image=calcimg,compound=LEFT)
        maths_button.grid(row=10,column=1)
        science_button = tk.Button(self.root, text = "Science",bg="white", command = self.setscience, font=wc_option_font,image=dnaimg,compound=LEFT)
        science_button.grid(row=11,column=1)
        history_button = tk.Button(self.root, text = "History",bg="white", command = self.sethistory, font=wc_option_font,image=feathimg,compound=LEFT)
        history_button.grid(row=12,column=1)
        geo_button = tk.Button(self.root, text = "Geography",bg="white", command = self.setgeo, font=wc_option_font,image=globeimg,compound=LEFT)
        geo_button.grid(row=13,column=1)
        astro_button = tk.Button(self.root, text = "Astronomy",bg="white", command = self.setastro, font=wc_option_font,image=starimg,compound=LEFT)
        astro_button.grid(row=14,column=1)
        
    def show_score(self):
        self.question_window1.destroy()
        for i in self.questions:
            print(i.tinyscore)
            self.score += i.tinyscore
        score_message = f"Your Final Score: {self.score}/5"
        messagebox.showinfo("Quiz Result", score_message)

swhoo=quiz(root)
root.mainloop()
