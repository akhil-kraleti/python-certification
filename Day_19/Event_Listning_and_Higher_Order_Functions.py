from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key = "space", fun = move_forward)
#onkey() is a Higher order function as it is able to work with other functions
# by taking them as inputs
screen.exitonclick()