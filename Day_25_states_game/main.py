import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
#Je kunt het in-statement alleen gebruiken als je de data naar een list hebt omgezet

scoreboard = Scoreboard()
game_is_on = True

while game_is_on == True:
    answer_state = screen.textinput(title="Guess a state", prompt="What's another state?").title()
    if answer_state == "Exit":
        states_to_learn = [s for s in all_states if s not in guessed_states]
        with open("states_to_learn.csv", "w") as file:
            file.write("\n".join(states_to_learn))
        #generate states_to_learn.csv
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        #Opgeslagen als rij met data, hier kun je data uit halen met de namen van de kolommen
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        scoreboard.increase_score()



