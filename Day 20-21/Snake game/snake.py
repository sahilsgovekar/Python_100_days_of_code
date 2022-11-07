from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.head.shape("circle")
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.addsegment(position)

    def addsegment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.addsegment(self.segment[-1].position())

    def move(self):
        for segn in range(len(self.segment)-1, 0, -1):
            newx = self.segment[segn-1].xcor()
            newy = self.segment[segn-1].ycor()
            self.segment[segn].goto(x=newx, y=newy)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)