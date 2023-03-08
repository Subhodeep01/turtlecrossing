import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
ticks = 0
flag = 0
inc = 1
MULTIPLIER = 0.3

screen = Screen()
player = Player()
car = [CarManager(flag)]
SB = Scoreboard()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ticks += inc
    if ticks >= 6:
        ticks = 0
        car.append(CarManager(flag))
    for cars in car:
        cars.movement()
        if cars.distance(player) < 20:
            game_is_on = False
            SB.game_over()

    if player.ycor() > FINISH_LINE_Y:
        player.refresh()
        flag += MULTIPLIER
        inc += MULTIPLIER * inc
        SB.inc_lvl()

screen.exitonclick()
