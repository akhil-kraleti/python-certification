from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)
angles = [0,90,180,270]



for _ in range(60):
    tim.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tim.pensize(1)
    tim.speed("fastest")
    tim.circle(100)
    tim.setheading(tim.heading() + 6)






screen.exitonclick()