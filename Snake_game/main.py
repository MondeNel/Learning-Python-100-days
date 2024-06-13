import turtle
import tkinter as tk
from tkinter import messagebox
import random

class Snake:
    '''Initializes the Snake object with an empty list of segments.
    Calls create_snake to create the initial snake.
    Sets the head of the snake to the first segment.
    Sets the initial direction of the snake to "stop".'''
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "stop"

    '''Defines the initial positions of the snake segments.
    Adds segments to the snake at the initial positions.'''
    def create_snake(self):
        initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in initial_positions:
            self.add_segment(position)

    '''Creates a new turtle segment.
    Sets the shape, color, and position of the segment.
    Adds the segment to the list of segments.'''
    def add_segment(self, position):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    '''Moves each segment to the position of the previous segment.
    Moves the head of the snake forward by 20 units.'''
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    '''Change the direction of the snake if it is not moving in the opposite direction.'''
    def up(self):
        if self.direction != "down":
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.direction = "down"

    def left(self):
        if self.direction != "right":
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.direction = "right"

    '''Changes the heading of the snake's head based on the current direction.'''
    def change_direction(self):
        if self.direction == "up":
            self.head.setheading(90)
        elif self.direction == "down":
            self.head.setheading(270)
        elif self.direction == "left":
            self.head.setheading(180)
        elif self.direction == "right":
            self.head.setheading(0)

class Snack:
    def __init__(self):
        self.snack = turtle.Turtle("circle")
        self.snack.color("red")
        self.snack.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.snack.goto(random_x, random_y)


'''Sets up the screen with a black background, a title, and a size of 600x600 pixels.
Disables automatic screen updates for smoother animation.'''
# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


'''Creates an instance of the Snake class.
Listens for keyboard input and binds the arrow keys to the snake's direction methods.'''
# Create the snake object
snake = Snake()

# Keyboard bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


'''Updates the snake's direction.
Moves the snake.
Updates the screen.
Repeats the game loop every 100 milliseconds.'''
# Function to start the game loop
def game_loop():
    snake.change_direction()
    snake.move()
    screen.update()
    screen.ontimer(game_loop, 100)


'''Creates a root window and hides it.
Displays a popup message asking the user to click "OK" to start the game.
Destroys the root window.
Starts the game loop.'''
# Function to show start message
def show_start_message():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Snake Game", "Click OK to start the game.")
    root.destroy()
    # Start the game loop after the user clicks OK
    game_loop()


'''Shows the start message and starts the game.
Keeps the window open and listens for events.'''
# Show the start message and then start the game
show_start_message()

# Keep the window open
screen.mainloop()
