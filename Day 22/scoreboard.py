from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.lscore, align="center", font=(80))
        self.goto(x=100, y=200)
        self.write(self.rscore, align="center", font=(80))

    def lpoint(self):
        self.lscore += 1
        self.updatescore()

    def rpoint(self):
        self.rscore += 1
        self.updatescore()