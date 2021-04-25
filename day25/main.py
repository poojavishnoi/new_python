import turtle
import pandas

screen = turtle.Screen()
screen.setup(800, 900)
screen.title("India State Game")
image = "final.gif"
screen.addshape(image)
turtle.shape(image)

file = pandas.read_csv("50_states.csv")
names = file.state.to_list()
guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 states", prompt="Enter the name of state.").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in names:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break
    if answer_state in names:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = file[file.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


