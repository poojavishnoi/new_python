from turtle import Turtle,Screen,colormode
import random

tim = Turtle()
tim.shape("classic")
tim.pensize()
color = colormode(255)


color_list = [(203, 165, 108), (152, 75, 48), (53, 93, 124), (223, 202, 135), (171, 153, 42), (137, 32, 20), (132, 163, 184), (47, 121, 86), (200, 90, 72), (72, 45, 36), (15, 98, 73), (97, 73, 75), (147, 180, 147), (164, 142, 157), (234, 175, 164), (55, 47, 50), (182, 205, 171), (155, 18, 23), (37, 61, 73), (22, 83, 89), (80, 147, 128)]
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

def new_line():
    for _ in range(10):
        for _ in range(10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)

        tim.setheading(90)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

new_line()

screen = Screen()
screen.exitonclick()
