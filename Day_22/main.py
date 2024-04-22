from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_running = True

#TODO 1: Create playing field

screen = Screen()
screen.bgcolor("black")
screen.screensize(800,600)
screen.title("Pong")
screen.bgcolor("orange")
screen.tracer(0)

#TODO 3: create and move paddle

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

#TODO 4: Create ball class with move methodes

ball = Ball()
scoreboard = Scoreboard()

while game_is_running:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

#TODO 5: detect collision with wall

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

#TODO 6: detect collision with paddle

    if ball.distance(right_paddle) < 45 and ball.xcor() > 340 or ball.distance(left_paddle) < 30 and ball.xcor() > -340:
        ball.bounce_x()

#TODO 7: right_paddle misses

    if ball.xcor() > 360:
        ball.reset()
        scoreboard.l_point()

 #TODO 8: left_paddle misses

    if ball.xcor() < -360:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()

