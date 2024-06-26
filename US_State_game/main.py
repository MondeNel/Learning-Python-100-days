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

# Timer
timer = 300  # 5 minutes in seconds
start_time = time.time()

# Score
score = 0

# Main game loop
while True:
    # Update the timer
    remaining_time = timer - (time.time() - start_time)
    if remaining_time <= 0:
        break  # Time's up, end the game

    # Update the screen title with the remaining time
    screen.title(f"U.S. States Game - Time: {int(remaining_time)}s - Score: {score}/50")

    # Ask for a guess
    if guess_state():
        score += 1

# Game over
screen.title("U.S. States Game - Game Over")
screen.textinput("Game Over", "Time's up! Press 'OK' to exit.")




# Kepp the screen open
turtle.mainloop()