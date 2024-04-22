import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.start_scoreboard()

#TODO: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left
# edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone
# for our little turtle). Hint: generate a new car only every 6th time the game loop runs.
    car_manager.create_car()
    car_manager.move_cars()

#TODO: Detect when the turtle player collides with a car and stop the game if this happens
    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

#TODO: Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this
# happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an
# attribute and using the MOVE_INCREMENT to increase the car speed.

    if turtle.ycor() == FINISH_LINE_Y:
        scoreboard.increase_score()
        turtle.reset()
        car_manager.increase_speed()

#TODO: Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a
# successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre

screen.exitonclick()