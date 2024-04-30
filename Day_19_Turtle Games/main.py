#The listen() method = luisteren naar wat de gebruiker doet.
from turtle import Turtle, Screen



# def move_forwards():
#     tim.forward(10)
#
# screen.listen()
# #event listener: luistert naar een specifieke toets die de gebruiker indrukt.
# screen.onkey(key="space", fun=move_forwards)
#let op: de functie in het event geef je geen haakjes mee

#basically is dit een functie die wordt gebruikt als input. Hier gebruik je dus geen haakjes op het einde.

#Higher order function = een functie die met andere functies kan werken (denk voorbeeld van de rekenmachine).
#nuttig bij event listeners. Gebruik keyword arguments als je de methode zelf niet hebt gecreerd (c=3)

def move_forward():
    new_turtle.forward(10)

def move_backward():
    new_turtle.backward(10)

def move_left():
    new_turtle.left(10)

def move_right():
    new_turtle.right(10)

def reset_screen():
    new_turtle.clear()
    new_turtle.reset()

def etch_a_sketch():
    screen = Screen()
    new_turtle.shape("turtle")
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_left)
    screen.onkey(key="a", fun=move_right)
    screen.onkey(key="d", fun=move_backward)
    screen.onkey(key="c", fun=reset_screen)
    screen.exitonclick()

def turtle_race():
    import random

    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-100, -75, -50, -25, 0, 25, 50]
    all_turtles = []

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-240, y=-y_positions[turtle_index])
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 220:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()

challenge = input("Which challenge you want to play? Press 1 for Etch a sketch, 2 for Turtle Race")
if challenge == "1":
    new_turtle = Turtle()
    etch_a_sketch()
elif challenge == "2":
    turtle_race()

#Voorbeelden van het object Turtle noem je instances. Dus timmy en tommy zijn instances van de turtle.
#Object state = de verschillende attributen of methodes van een object
