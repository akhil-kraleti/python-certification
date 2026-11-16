from turtle import Turtle, Screen
import random
#import colorgram
#
#rgb_colors = []
#colors = colorgram.extract('dot_paint.jpg',30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)
color_list = [(231, 206, 85), (231, 222, 226), (224, 150, 89), (215, 224, 230), (120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144), (8, 97, 38), (171, 21, 16), (199, 65, 28), (185, 186, 27), (31, 128, 47), (12, 41, 74), (15, 63, 40), (242, 202, 5), (138, 82, 95), (85, 15, 22), (51, 166, 77), (44, 26, 22), (6, 65, 137), (173, 135, 149), (232, 170, 160), (48, 150, 195), (219, 66, 71), (74, 135, 186), (169, 206, 175), (70,60,60)]

tim.setheading(223)
tim.up()
tim.forward(320)
tim.down()
tim.setheading(0)

for i in range(10):
    for j in range(10):

        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.up()
        tim.forward(50)
        tim.down()
    tim.setheading(90)
    tim.up()
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    tim.down()

screen.exitonclick()