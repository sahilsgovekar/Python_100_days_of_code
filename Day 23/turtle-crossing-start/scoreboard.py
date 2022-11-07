from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

        self.lvl = 0
        self.update_score()
        


    def update_score(self):
        self.clear()
        self.goto(0, 300)
        self.write(f"Level {self.lvl}", align="center", font=(FONT))

    def increse_score(self):
        self.lvl += 1
        self.update_score()
