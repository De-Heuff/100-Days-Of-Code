from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = random.randint(0,10)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1.1

    def reset(self):
        self.home()
        self.x_move *= -1
        self.move_speed = 0.1









