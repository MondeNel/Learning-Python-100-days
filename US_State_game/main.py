import turtle
import pandas as pd
import time

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)

# Load the background image
screen.bgpic("blank_states_img.gif")

# Set up the turtle for writing state names
state_writer = turtle.Turtle()
state_writer.penup()
state_writer.hideturtle()

# Load the CSV data
data = pd.read_csv("50_states.csv")
states_dict = {row["state"]: (row["x"], row["y"]) for index, row in data.iterrows()}

# Function to move the state name to its position on the map
def move_state_name(state_name):
    state_writer.goto(states_dict[state_name])
    state_writer.write(state_name, align="center", font=("Arial", 8, "normal"))


# Function to ask the user for a state name and move it if correct
def guess_state():
    user_input = screen.textinput("Guess the State", "Enter a state name (or 'exit' to quit):").title()
    if user_input == "Exit":
        return False
    if user_input in states_dict:
        move_state_name(user_input)
    return True

# Keep asking for guesses until the user exits
while guess_state():
    pass






# Kepp the screen open
turtle.mainloop()