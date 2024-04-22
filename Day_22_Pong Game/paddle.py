from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def move_down(self):
        self.backward(MOVE_DISTANCE)












