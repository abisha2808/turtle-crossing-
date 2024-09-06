from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level =1
        self.goto(x=-250, y=250)
        self.write(f"level: {self.level}",align="left",font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
