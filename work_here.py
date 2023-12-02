from tkinter import messagebox
import pandas as pd
import random
import tkinter as tk

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
            self.tinyscore += 1
            print("correct")
        else:
            print("wrong")
    def check2(self):
        if self.option2 == self.correct_answer:
            self.tinyscore += 1
            print("correct")
        else:
            print("Wrong")
    def check3(self):
        if self.option3 == self.correct_answer:
            self.tinyscore += 1
            print("correct")
        else:
            print("wrong")
    def check4(self):
        if self.option4 == self.correct_answer:
            self.tinyscore += 1
            print("correct")
        else:
            print("wrong")
            
        

def selectq(subject):
    df = pd.read_csv("quiz_questions.csv")
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
    

    def xyz(self): 
        self.startquiz(self.subject)

    def displayquestion1(self):
        self.question_window1 = tk.Toplevel(self.root)
        question_label = tk.Label(self.question_window1, text=self.questions[0].question_statement)
        question_label.pack()

        option1_button = tk.Button(self.question_window1, text=self.questions[0].option1, command=self.questions[0].check1)
        option1_button.pack()

        option2_button = tk.Button(self.question_window1, text=self.questions[0].option2, command=self.questions[0].check2)
        option2_button.pack()

        option3_button = tk.Button(self.question_window1, text=self.questions[0].option3, command=self.questions[0].check3)
        option3_button.pack()

        option4_button = tk.Button(self.question_window1, text=self.questions[0].option4, command=self.questions[0].check4)
        option4_button.pack()

        next_button = tk.Button(self.question_window1, text = "Next", command = self.displayquestion2)
        next_button.pack()

        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]
    def displayquestion2(self):
        for i in self.widgets:
            i.destroy()
        question_label = tk.Label(self.question_window1, text=self.questions[1].question_statement)
        question_label.pack()

        option1_button = tk.Button(self.question_window1, text=self.questions[1].option1, command=self.questions[1].check1)
        option1_button.pack()

        option2_button = tk.Button(self.question_window1, text=self.questions[1].option2, command=self.questions[1].check2)
        option2_button.pack()

        option3_button = tk.Button(self.question_window1, text=self.questions[1].option3, command=self.questions[1].check3)
        option3_button.pack()

        option4_button = tk.Button(self.question_window1, text=self.questions[1].option4, command=self.questions[1].check4)
        option4_button.pack()

        next_button = tk.Button(self.question_window1, text = "Next", command = self.displayquestion3)
        next_button.pack()
        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    def displayquestion3(self):
        for i in self.widgets:
            i.destroy()

        option1_button = tk.Button(self.question_window1, text=self.questions[2].option1, command=self.questions[2].check1)
        option1_button.pack()

        option2_button = tk.Button(self.question_window1, text=self.questions[2].option2, command=self.questions[2].check2)
        option2_button.pack()

        option3_button = tk.Button(self.question_window1, text=self.questions[2].option3, command=self.questions[2].check3)
        option3_button.pack()

        option4_button = tk.Button(self.question_window1, text=self.questions[2].option4, command=self.questions[2].check4)
        option4_button.pack()

        next_button = tk.Button(self.question_window1, text = "Next", command = self.displayquestion4)
        next_button.pack()
        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    def displayquestion4(self):
        for i in self.widgets:
            i.destroy()
        question_label = tk.Label(self.question_window1, text=self.questions[3].question_statement)
        question_label.pack()

        option1_button = tk.Button(self.question_window1, text=self.questions[3].option1, command=self.questions[3].check1)
        option1_button.pack()

        option2_button = tk.Button(self.question_window1, text=self.questions[3].option2, command=self.questions[3].check2)
        option2_button.pack()

        option3_button = tk.Button(self.question_window1, text=self.questions[3].option3, command=self.questions[3].check3)
        option3_button.pack()

        option4_button = tk.Button(self.question_window1, text=self.questions[3].option4, command=self.questions[3].check4)
        option4_button.pack()

        next_button = tk.Button(self.question_window1, text = "Next", command = self.displayquestion5)
        next_button.pack()
        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    def displayquestion5(self):
        for i in self.widgets:
            i.destroy()
        question_label = tk.Label(self.question_window1, text=self.questions[4].question_statement)
        question_label.pack()

        option1_button = tk.Button(self.question_window1, text=self.questions[4].option1, command=self.questions[4].check1)
        option1_button.pack()

        option2_button = tk.Button(self.question_window1, text=self.questions[4].option2, command=self.questions[4].check2)
        option2_button.pack()

        option3_button = tk.Button(self.question_window1, text=self.questions[4].option3, command=self.questions[4].check3)
        option3_button.pack()

        option4_button = tk.Button(self.question_window1, text=self.questions[4].option4, command=self.questions[4].check4)
        option4_button.pack()

        next_button = tk.Button(self.question_window1, text = "End Quiz", command = self.show_score)
        next_button.pack()
        self.widgets=[question_label, option1_button, option2_button, option3_button, option4_button, next_button]

    
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
        start = tk.Button(root, text = "Start quiz", command = self.xyz)
        start.pack()
        subject_label = tk.Label(self.root, text="Select Subject:")
        subject_label.pack()
        all_button = tk.Button(self.root, text = "Any")
        all_button.pack()
        maths_button = tk.Button(self.root, text = "Maths", command = self.setmaths)
        maths_button.pack()
        science_button = tk.Button(self.root, text = "Science", command = self.setscience)
        science_button.pack()
        history_button = tk.Button(self.root, text = "History", command = self.sethistory)
        history_button.pack()
        geo_button = tk.Button(self.root, text = "Geography", command = self.setgeo)
        geo_button.pack()
        astro_button = tk.Button(self.root, text = "Astronomy", command = self.setastro)
        astro_button.pack()
        
    
    def show_score(self):
        self.question_window1.destroy()
        for i in self.questions:
            self.score += i.tinyscore
        score_message = f"Your Final Score: {self.score}/5"
        messagebox.showinfo("Quiz Result", score_message)

swhoo=quiz(root)
root.mainloop()
