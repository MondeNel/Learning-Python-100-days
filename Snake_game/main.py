import turtle
import tkinter as tk
from tkinter import messagebox

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "stop"

    def create_snake(self):
        initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in initial_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

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

    def change_direction(self):
        if self.direction == "up":
            self.head.setheading(90)
        elif self.direction == "down":
            self.head.setheading(270)
        elif self.direction == "left":
            self.head.setheading(180)
        elif self.direction == "right":
            self.head.setheading(0)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the snake object
snake = Snake()

# Keyboard bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Function to start the game loop
def game_loop():
    snake.change_direction()
    snake.move()
    screen.update()
    screen.ontimer(game_loop, 100)

# Function to show start message
def show_start_message():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Snake Game", "Click OK to start the game.")
    root.destroy()
    # Start the game loop after the user clicks OK
    game_loop()

# Show the start message and then start the game
show_start_message()

# Keep the window open
screen.mainloop()
