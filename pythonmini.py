from tkinter import messagebox
import pandas as pd
import random
import tkinter as tk

class Question:
    def __init__(self, row):
        self.question_statement = row['Question']
        self.options = [row['Option1'], row['Option2'], row['Option3'], row['Option4']]
        self.correct_answer = row['Correct answer']

def selectq(subject):
    df = pd.read_csv(r"C:\Users\VANSHIKA\Downloads\quiz_questions - Sheet1 (1).csv")
    if subject == "all":
        subject_questions = df
    else:
        subject_questions = df[df['subject'] == subject]
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
        
        
    def check(self, question, selected):
        if selected == question.correct_answer:
            self.score += 1

    def xyz(self): 
        self.startquiz(self.subject)

    def showquestion(self,i):
        question_window = tk.Toplevel(self.root)
        question_window.title("Question")
        question = tk.Label(question_window,text = i.question_statement)
        question.pack()
        for option in i.options:
            option_button = tk.Button(question_window, text = option, command = lambda : self.check(i, option))
            option_button.pack()
        #next_button = tk.Button(question_window, text="Next", command=question_window.destroy)
        #next_button.pack()
        print(self.score)
        print("showq called")

    def startquiz(self, sub):
        questions = selectq(sub)
        for i in questions:
            self.showquestion(i)
        self.show_score()

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
        score_message = f"Your Final Score: {self.score}/5"
        messagebox.showinfo("Quiz Result", score_message)

swhoo=quiz(root)
root.mainloop()
