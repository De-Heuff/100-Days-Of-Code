FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 260)

    def start_scoreboard(self):
        self.write(arg=f"SCORE: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.start_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="YOU DIED", align="center", font=FONT)




