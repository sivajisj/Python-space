from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
def move_fwd():
    tim.fd(20)
def move_bwd():
    tim.backward(20)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()

screen.listen()

screen.onkey(key="w", fun=move_fwd)
screen.onkey(key="s", fun=move_bwd)
screen.onkey(key= "a", fun= turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
