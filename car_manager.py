from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
XCOR = 300


class CarManager(Turtle):
    def __init__(self, spd):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.spawn()
        self.move_speed = STARTING_MOVE_DISTANCE + spd * MOVE_INCREMENT

    def spawn(self):
        y = random.randint(-250, 250)
        self.goto(x=XCOR, y=y)

    def movement(self):
        self.forward(self.move_speed)

