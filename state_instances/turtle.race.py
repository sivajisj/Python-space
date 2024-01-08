import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "blue", "purple", "orange",  "gray", "teal", "cyan", ]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
all_turtles = []


for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(random.choice(colors))
    new_turtle.goto(-200,-100 + (i * 45))
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
     for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won!, the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()