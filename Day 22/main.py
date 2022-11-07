from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

ball = Ball()
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

l_paddle = Paddle((-350, 0))
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game = True
t = 0.1
while game:
    screen.update()
    time.sleep(t)
    ball.moveball()
    if ball.ycor() > 290 or ball.ycor() <= -290:
        t *= 0.9
        ball.bounce_y()
    
    #colusion with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        t *= 0.999
        ball.bounce_x()
    

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.lpoint()
        t = 0.1

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.rpoint()
        t = 0.1

        
    




screen.exitonclick()