import turtle

import pandas

screen = turtle.Screen()
screen.title("us state game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle.penup

data = pandas.read_csv("50_states.csv")

list = data["state"].tolist()
guessed_state = []
while len(guessed_state) <50:
    answer_state = screen.textinput(title=f"Guess left {len(guessed_state)}/50", prompt="Whats next state")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        gussed = data[data.state == answer_state]
        t.goto(x=int(gussed["x"]), y=int(gussed["y"]))
        t.write(answer_state)
        guessed_state.append(answer_state)

not_guessed = []
for i in list:
    if i not in guessed_state:
        not_guessed.append(i)

not_guessed_data = pandas.DataFrame(not_guessed)
print(f"Not Guessed states are \n {not_guessed_data}")
not_guessed_data.to_csv("not_guessed_data.csv")