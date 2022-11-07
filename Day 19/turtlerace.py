from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

race = False

tcolor = ["red", "yellow", "blue", "brown", "green", "pink", "purple"]
tpos = [-150, -100, -50, 0, 50, 100, 150]
turtles = []


user_bet = screen.textinput(title="Place your bet", prompt="Red, Yellow, Blue, Brown, Green, Pink, purple Select color to place the bet")
#print(user_bet)

for turin in range(0, 7):
    obj = Turtle(shape="turtle")
    obj.color(tcolor[turin])
    obj.penup()
    obj.goto(x=-230, y=tpos[turin])
    turtles.append(obj)



if user_bet:
    race = True

while race:
    for t in turtles:
        if t.xcor() > 230:
            race = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print("You Won The Bet")
            else:
                print("You Lost The Bet")
        random_distance = random.randint(0, 10)
        t.forward(random_distance)


screen.exitonclick()