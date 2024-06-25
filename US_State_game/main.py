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

# Function to display state on the map
def mouse_click_coordinates(x, y):
    print(x, y)
    

turtle.onscreenclick(mouse_click_coordinates)

turtle.mainloop()