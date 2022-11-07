from turtle import Turtle, xcor

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("purple")
        # self.dir = "up"
        self.x_move = 10
        self.y_move = 10

    def moveball(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(x=newx, y=newy)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()

        
    # def moveball(self):
    #     if self.dir == "up":
    #         newx = self.xcor() + 20
    #         newy = self.ycor() + 20
    #         self.goto(x=newx, y=newy)
    #     else:
    #         newx = self.xcor() + 20
    #         newy = self.ycor() - 20
    #         self.goto(x=newx, y=newy)

    #     if self.xcor() >= 275:
    #         self.dir = "down"
    #     elif self.xcor() <= -275:
    #         self.dir = "up"

        