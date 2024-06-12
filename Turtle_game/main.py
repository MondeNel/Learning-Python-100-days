
import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(1)  # You can set the speed from 1 (slow) to 10 (fastest) or 0 (no animation)


# Function to move the turtle forward
def move_forward():
    t.forward(20)

# Function to move the turtle backward
def move_backward():
    t.backward(20)

# Function to turn the turtle counterclockwise
def turn_left():
    t.left(15)

# Function to turn the turtle clockwise
def turn_right():
    t.right(15)

# Function to clear the drawing
def clear_drawing():
    t.clear()


# Create a screen object
screen = turtle.Screen()
screen.title("Turtle Control with Keyboard")

# Listen for key presses
screen.listen()