from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.color("green")
        self.shapesize(2, 2)
        self.goto(STARTING_POSITION)

    def goup(self):
        self.forward(MOVE_DISTANCE)

    def godown(self):
        self.backward(MOVE_DISTANCE)

    def goleft(self):
        newx = self.xcor() - MOVE_DISTANCE
        newy = self.ycor()
        self.goto(x=newx, y=newy)

    def goright(self):
        newx = self.xcor() + MOVE_DISTANCE
        self.goto(newx, self.ycor())

    def levelup(self):
        self.goto(STARTING_POSITION)

    def check_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

