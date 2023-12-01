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

class quiz:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.root.title("Quiz")
        self.subject = "all"
        self.welcomescreen()
        self.x = True
        self.questions = []
    

    def xyz(self): 
        self.startquiz(self.subject)

    
    def startquiz(self, sub):
        self.questions = selectq(sub)
        question_window = tk.Toplevel(self.root)
        option1_button = [0,0,0,0,0]
        option2_button = [0,0,0,0,0]
        option3_button = [0,0,0,0,0]
        option4_button = [0,0,0,0,0]

        for i in range(5):
            question_label = tk.Label(question_window, text=self.questions[i].question_statement)
            question_label.pack()

            option1_button[i] = tk.Button(question_window, text=self.questions[i].option1, command=self.questions[i].check1)
            option1_button[i].pack()

            option2_button[i] = tk.Button(question_window, text=self.questions[i].option2, command=self.questions[i].check2)
            option2_button[i].pack()

            option3_button[i] = tk.Button(question_window, text=self.questions[i].option3, command=self.questions[i].check3)
            option3_button[i].pack()

            option4_button[i] = tk.Button(question_window, text=self.questions[i].option4, command=self.questions[i].check4)
            option4_button[i].pack()

            #self.score += self.questions[i].tinyscore

        end_button = tk.Button(question_window, text="End quiz", command=self.show_score)
        end_button.pack()
        
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
        for i in self.questions:
            self.score += i.tinyscore
        score_message = f"Your Final Score: {self.score}/5"
        messagebox.showinfo("Quiz Result", score_message)

swhoo=quiz(root)
root.mainloop()