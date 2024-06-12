
import turtle
import random

# Define the RacingTurtle class
class RacingTurtle:
    def __init__(self, color, y_position):
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.goto(-230, y_position)

    def move_forward(self):
        self.turtle.forward(random.randint(1, 10))

    def get_x_position(self):
        return self.turtle.xcor()

# Function to move the user-controlled turtle
def user_move():
    user_turtle.turtle.forward(10)


# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
