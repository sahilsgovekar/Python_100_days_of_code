from turtle import Turtle, Screen
import random
obj = Turtle()
# obj.width(20)
on = Screen()



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255) 
    color = (r, g, b)
    return color

def cr(size):
    for i in range(360 / size):
        obj.color(random_color())
        obj.circle(100)
        obj.setheading(obj.heading()+size)

cr(25)


on.exitonclick()