from turtle import Turtle, Screen
import turtle
import random

turt = Turtle()

turtle.colormode(255)
turt.hideturtle()
turt.speed('fastest')

height = -240

turt.penup()
turt.goto(-240, height)

for i in range(10):
    for j in range(10):
        turt.dot(20, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        turt.penup()
        turt.forward(50)
        turt.pendown
    turt.penup()
    height += 50
    turt.goto(-240, height)
    
screen = Screen()
screen.exitonclick()