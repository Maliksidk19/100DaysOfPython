import pandas as pd
import turtle
from turtle import Screen

screen = Screen()
screen.title("US. states Game")
screen.setup(width=725, height=491)
image = "Files/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

data = pd.read_csv("Files/50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name? ")

    if answer_state == "exit":
        remaining_states = []

        for states in all_states:
            if states not in guessed_states:
                remaining_states.append(states)

        df = pd.DataFrame(remaining_states)
        df.to_csv("Files/Missing_States.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)

screen.exitonclick()
