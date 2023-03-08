from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=260)
        self.lvl = 0
        self.write(arg=f"Level: {self.lvl}", align="left", font=FONT)

    def inc_lvl(self):
        self.lvl += 1
        self.clear()
        self.write(arg=f"Level: {self.lvl}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="left", font=FONT)
