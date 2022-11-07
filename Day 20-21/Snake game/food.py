from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rx = random.randint(-280, 280)
        ry = random.randint(-280, 280)
        self.goto(x=rx, y=ry)

    def bigf(self):
        self.color("red")
        self.shapesize(stretch_len=5, stretch_wid=5)
        rx = random.randint(-280, 280)
        ry = random.randint(-280, 280)
        self.goto(x=rx, y=ry)

