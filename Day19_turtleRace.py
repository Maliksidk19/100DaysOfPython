# <<<<< IMPORTS >>>>>
from turtle import Turtle, Screen
import random

# <<<<< VARIABLES >>>>>
turtles = []
dists = []
x_axis = -230
y_axis = -120
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def draw_winning_line():
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.setheading(270)
    line.goto(x=200, y=150)
    line.pendown()
    line.forward(300)
    
def instaniate_turtles(y_axis):
    for i in colors:
        tim = Turtle(shape="turtle")
        tim.color(i)
        tim.penup()
        tim.goto(x=x_axis, y=y_axis)
        turtles.append(tim)
        y_axis += 50
        
def race_result():
    for turt in turtles:
        if turt.xcor() > 200:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The \033[1;34m{winning_color}\033[m turtle is the winner!")
                exit()
            else:
                print(f"You've lost! The \033[1;34m{winning_color}\033[m turtle is the winner!")
                exit()


screen = Screen()
screen.title("Python Turtle Race")
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

draw_winning_line()

instaniate_turtles(y_axis)
 
if user_bet:
    is_race_on = True   
    
while is_race_on and x_axis < 180:
    race_result() 
        
    for turtle in turtles:
        dist = random.randint(0,10)
        dists.append(dist)
        turtle.forward(dist)
    x_axis += (sum(dists) / len(dists))

screen.exitonclick()