from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cor)
        
    def go_up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def go_down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)

