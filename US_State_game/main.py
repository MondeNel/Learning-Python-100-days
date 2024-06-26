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

# Track guessed states
guessed_states = []

# Function to move the state name to its position on the map
def move_state_name(state_name):
    state_writer.goto(states_dict[state_name])
    state_writer.write(state_name, align="center", font=("Arial", 8, "normal"))

# Function to ask the user for a state name and move it if correct
def guess_state():
    user_input = screen.textinput("Guess the State", "Enter a state name (or 'exit' to quit):").title()
    if user_input == "Exit":
        return False
    if user_input in states_dict and user_input not in guessed_states:
        move_state_name(user_input)
        guessed_states.append(user_input)
    return True

# Create a turtle for the countdown timer
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, 260)

# Create a turtle for the scoreboard
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 280)

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

    # Update the timer display
    timer_turtle.clear()
    timer_turtle.write(f"Time: {int(remaining_time)}s", align="center", font=("Arial", 16, "normal"))

    # Update the scoreboard display
    score_turtle.clear()
    score_turtle.write(f"Score: {score}/50", align="center", font=("Arial", 16, "normal"))

    # Ask for a guess
    if not guess_state():
        break  # User chose to exit

    score = len(guessed_states)

# Game over
screen.title("U.S. States Game - Game Over")
missing_states = [state for state in states_dict.keys() if state not in guessed_states]
print(f"Missing States: {', '.join(missing_states)}")

# Save missing states to a CSV file
missing_states_df = pd.DataFrame(missing_states, columns=["Missing States"])
missing_states_df.to_csv("missing_states.csv", index=False)

screen.textinput("Game Over", f"Time's up! Missing States saved to missing_states.csv. Press 'OK' to exit.")

# Keep the screen open
turtle.mainloop()
