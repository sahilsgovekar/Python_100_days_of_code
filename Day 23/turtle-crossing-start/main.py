import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.goup, "Up")
screen.onkey(player.godown, "Down")
screen.onkey(player.goleft, "Left")
screen.onkey(player.goright, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.createcars()
    car_manager.movecar()

    for i in car_manager.cars:
        if i.distance(player) < 25:
            game_is_on = False

    if player.check_level():
        player.levelup()
        car_manager.newcarspeed()
        scoreboard.increse_score()

screen.exitonclick()