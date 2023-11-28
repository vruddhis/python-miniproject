#import fromdataset.py
import tkinter as tk
root = tk.Tk()
##selected_questions gives a list of questions. every question in the list has the attributes question_statement q.options (a list of 4 options) and q.correct_answer

#labelsforsubjects
#def select_subject:
#sub = select_subject()
class quiz:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.root.title("Quiz")
        #select subject
        self.welcomescreen()

        
    def check(self, question, selected):
        if selected == question.correct_answer:
            self.score += 1

    def showquestion(self,i):
        question_window = tk.Toplevel(self.root)
        question_window.title("Question" + i+1)
        question = tk.Label(question_window,text = i.question_statement)
        question.pack()
        for option in i.options:
            option_button = tk.Button(question_window, text = option, command = lambda selected = option: self.check(i, selected))
        question_window.destroy()
        
    def startquiz(self):
        questions = fromdataset.selectq(sub)
        for i in questions:
            self.showquestion(i)
        final_score_label = tk.Label(self.root, text=f"Your Final Score: {self.score}/10")
        final_score_label.pack()







    def welcomescreen:
        start = Button(root, text = "Start quiz", command = self.startquiz)
    


quiz(root)
root.mainloop()