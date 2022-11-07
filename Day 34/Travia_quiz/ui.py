from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        




        self.scor = Label(text="Score", fg="white", bg=THEME_COLOR)
        self.scor.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.Q_text = self.canvas.create_text(150, 125, text="questions", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, rowspan=2)

        self.ri_i = PhotoImage(file="images/true.png")
        self.wr_i = PhotoImage(file="images/false.png")    
        self.but_r = Button(image=self.ri_i, padx=20, pady=20, highlightthickness=0, command=self.righta)
        self.but_r.grid(column=0, row=3)    
        self.but_w = Button(image=self.wr_i, highlightthickness=0, command=self.wronga)
        self.but_w.grid(column=1, row=3)    

        self.get_next()

        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scor.config(text=f"Score : {self.quiz.score}")
            nq_text = self.quiz.next_question()
            self.canvas.itemconfig(self.Q_text, text=nq_text)
        else:
            self.canvas.itemconfig(self.Q_text, text="Game Ended")
            self.but_r(state="disabled")
            self.but_w(state="disabled")

    def righta(self):
            self.feed = self.quiz.check_answer("true")
            self.userfeedback(self.feed)
    
    def wronga(self):
            self.feed = self.quiz.check_answer("false")
            self.userfeedback(self.feed)

    def userfeedback(self, feedback):
        if feedback:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next)

