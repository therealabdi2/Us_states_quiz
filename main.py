import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").capitalize()
    if answer_state == "Exit":
        missed_states =[state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_info = data[data.state == answer_state]
        state_xcor = int(state_info.x)
        state_ycor = int(state_info.y)
        state_pos = (state_xcor, state_ycor)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.setposition(state_pos)
        t.write(f"{state_info.state.item()}", align="center", font=("Courier", 7, "bold"))





screen.exitonclick()
