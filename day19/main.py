from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle you think would win the game.\n (violet/blue/green/yellow/orange/red")
color_list = ["violet", "blue", "green", "yellow", "orange", "red"]
y = [70, 40, 10, -30, -60, -90]
all_turtle = []
repeat = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(-200, y=y[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    repeat = True

while repeat:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            repeat = False
            winning_color = turtle.pencolor()
            if user_bet == turtle.pencolor():
                print(f"You won.The winning color is {winning_color}")
            else:
                print(f"You lose.The winning color is {winning_color}")


        turtle.forward(random.randint(0,10))


screen.exitonclick()
