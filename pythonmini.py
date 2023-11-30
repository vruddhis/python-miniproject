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
    df = pd.read_csv(r"C:\Users\VANSHIKA\Downloads\quiz_questions - Sheet1 (1).csv")
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
    

    def xyz(self): 
        self.startquiz(self.subject)

    def startquiz(self, sub):
    questions = selectq(sub)
    question_window = tk.Toplevel(self.root)
    question1 = tk.Label(question_window, text=questions[0].question_statement)
    question1.pack()
    oA1 = tk.Button(question_window, text=questions[0].option1, command=questions[0].check1)
    oA1.pack()
    oB1 = tk.Button(question_window, text=questions[0].option2, command=questions[0].check2)
    oB1.pack()
    oC1 = tk.Button(question_window, text=questions[0].option3, command=questions[0].check3)
    oC1.pack()
    oD1 = tk.Button(question_window, text=questions[0].option4, command=questions[0].check4)
    oD1.pack()

    question2 = tk.Label(question_window, text=questions[1].question_statement)
    question2.pack()
    oA2 = tk.Button(question_window, text=questions[1].option1, command=questions[1].check1)
    oA2.pack()
    oB2 = tk.Button(question_window, text=questions[1].option2, command=questions[1].check2)
    oB2.pack()
    oC2 = tk.Button(question_window, text=questions[1].option3, command=questions[1].check3)
    oC2.pack()
    oD2 = tk.Button(question_window, text=questions[1].option4, command=questions[1].check4)
    oD2.pack()

    question3 = tk.Label(question_window, text=questions[2].question_statement)
    question3.pack()
    oA3 = tk.Button(question_window, text=questions[2].option1, command=questions[2].check1)
    oA3.pack()
    oB3 = tk.Button(question_window, text=questions[2].option2, command=questions[2].check2)
    oB3.pack()
    oC3 = tk.Button(question_window, text=questions[2].option3, command=questions[2].check3)
    oC3.pack()
    oD3 = tk.Button(question_window, text=questions[2].option4, command=questions[2].check4)
    oD3.pack()

    question4 = tk.Label(question_window, text=questions[3].question_statement)
    question4.pack()
    oA4 = tk.Button(question_window, text=questions[3].option1, command=questions[3].check1)
    oA4.pack()
    oB4 = tk.Button(question_window, text=questions[3].option2, command=questions[3].check2)
    oB4.pack()
    oC4 = tk.Button(question_window, text=questions[3].option3, command=questions[3].check3)
    oC4.pack()
    oD4 = tk.Button(question_window, text=questions[3].option4, command=questions[3].check4)
    oD4.pack()

    question5 = tk.Label(question_window, text=questions[4].question_statement)
    question5.pack()
    oA5 = tk.Button(question_window, text=questions[4].option1, command=questions[4].check1)
    oA5.pack()
    oB5 = tk.Button(question_window, text=questions[4].option2, command=questions[4].check2)
    oB5.pack()
    oC5 = tk.Button(question_window, text=questions[4].option3, command=questions[4].check3)
    oC5.pack()
    oD5 = tk.Button(question_window, text=questions[4].option4, command=questions[4].check4)
    oD5.pack()

    self.score += questions[0].tinyscore + questions[1].tinyscore + questions[2].tinyscore + questions[3].tinyscore + questions[4].tinyscore
    end = tk.Button(question_window, text="End quiz", command=self.show_score)
    end.pack()

        
        
        
        

    
        
        
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
