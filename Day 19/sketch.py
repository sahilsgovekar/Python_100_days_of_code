from turtle import Turtle, Screen


#object creation
obj = Turtle()
screen = Screen()

def front():
    obj.forward(10)

def back():
    obj.backward(10)

def cclock():
    obj.left(10)

def clock():
    obj.right(10)

def clean():
    obj.clear()
    obj.penup()
    obj.home()
    obj.pendown()


screen.listen()
screen.onkey(key="w", fun=front)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=cclock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clean)


screen.exitonclick()