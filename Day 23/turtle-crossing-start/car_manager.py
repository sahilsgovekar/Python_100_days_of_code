from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def createcars(self):
        car_chance = random.randint(1, 6)
        if car_chance == 1:
            newcar = Turtle("square")
            newcar.penup()
            newcar.color(random.choice(COLORS))
            newcar.shapesize(stretch_len=2, stretch_wid=1)
            newy = random.randint(-250, 250)
            newcar.goto(x=300, y=newy)
            self.cars.append(newcar)

    def movecar(self):
        for i in self.cars:
            i.backward(self.carspeed)

    def newcarspeed(self):
        self.carspeed += MOVE_INCREMENT


