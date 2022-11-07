from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


game = True
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detectin collusion
    if snake.head.distance(food) < 15:
        food.refresh()
        score.addscore()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game = False
        score.busted()

    for seg in snake.segment[1:]:
        if snake.head.distance(seg) <10:
            game = False
            score.busted()


    
    

screen.exitonclick()