from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.cscore = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"SCORE {self.cscore}", True, align = "center")

    def addscore(self):
        self.cscore += 1
        self.clear()
        self.write(f"SCORE {self.cscore}", True, align = "center")

    def busted(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", True, align = "center")

        