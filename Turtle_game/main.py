import turtle
import random
import time
import tkinter as tk
from tkinter import messagebox

# Define the RacingTurtle class
class RacingTurtle:
    def __init__(self, color, y_position):
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.goto(-230, y_position)
        self.turtle.speed("fast")

    def move_forward(self):
        self.turtle.forward(random.randint(1, 10))

    def get_x_position(self):
        return self.turtle.xcor()

def user_move():
    user_turtle.turtle.forward(10)

def display_countdown():
    countdown_turtle = turtle.Turtle()
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.goto(0, 0)
    countdown_turtle.write("3", align="center", font=("Arial", 24, "normal"))
    time.sleep(1)
    countdown_turtle.clear()
    countdown_turtle.write("2", align="center", font=("Arial", 24, "normal"))
    time.sleep(1)
    countdown_turtle.clear()
    countdown_turtle.write("1", align="center", font=("Arial", 24, "normal"))
    time.sleep(1)
    countdown_turtle.clear()
    countdown_turtle.write("Go!", align="center", font=("Arial", 24, "normal"))
    time.sleep(1)
    countdown_turtle.clear()

def start_race():
    display_countdown()

    race_on = True

    while race_on:
        for racing_turtle in turtles:
            if racing_turtle != user_turtle:
                racing_turtle.move_forward()

            if racing_turtle.get_x_position() >= 230:
                race_on = False
                winner_color = racing_turtle.turtle.pencolor()
                root = tk.Tk()
                root.withdraw()  # Hide the root window
                play_again = messagebox.askyesno("Race Over", f"The winner is the {winner_color} turtle!\nDo you want to play again?")
                if play_again:
                    reset_race()
                else:
                    turtle.bye()
                break

def reset_race():
    for racing_turtle in turtles:
        racing_turtle.turtle.goto(-230, racing_turtle.turtle.ycor())
    user_choice_and_start()

def user_choice_and_start():
    global user_turtle

    user_choice = screen.textinput("Choose your turtle", "Enter a color (red, blue, green, yellow, purple): ").lower()
    user_turtle = None

    for racing_turtle in turtles:
        if racing_turtle.turtle.color()[0] == user_choice:
            user_turtle = racing_turtle
            break

    if not user_turtle:
        print("Invalid choice. Defaulting to the red turtle.")
        user_turtle = turtles[0]

    # Popup for starting the race
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    if messagebox.askokcancel("Turtle Race", "Click OK to start the race"):
        display_countdown()
        screen.listen()
        screen.onkey(user_move, "space")
        start_race()

# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")

# Create the racing turtles
colors = ["red", "blue", "green", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50]
turtles = []

for i in range(5):
    turtles.append(RacingTurtle(colors[i], y_positions[i]))

# Draw the starting and finishing lines
start_line = turtle.Turtle()
start_line.penup()
start_line.goto(-250, -100)
start_line.pendown()
start_line.goto(-250, 100)
start_line.hideturtle()

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(230, -100)
finish_line.pendown()
finish_line.goto(230, 100)
finish_line.hideturtle()

# Ask the user to select a turtle and start the race
user_choice_and_start()

screen.mainloop()
