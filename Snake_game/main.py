'''turtle: Used for creating graphics and the game window.
    tkinter: Used for creating popup messages.
    random: Used for generating random positions for the snack.'''
import turtle
import tkinter as tk
from tkinter import messagebox
import random


'''init: Initializes the snake with three segments, sets the head of the snake, and the initial direction to "stop".
    create_snake: Creates the initial three segments of the snake.
    add_segment: Adds a new segment to the snake at the specified position.
    move: Moves the snake forward by updating the position of each segment to the position of the previous segment.
    grow: Adds a new segment to the snake at the position of the last segment.
    up, down, left, right: Changes the direction of the snake if the current direction is not opposite.
    change_direction: Sets the heading of the snake based on the current direction.'''
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

    def grow(self):
        last_segment_position = self.segments[-1].position()
        self.add_segment(last_segment_position)

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


'''init: Initializes the snack as a red circle and places it at a random position on the screen.
refresh: Moves the snack to a new random position within the screen bounds.'''
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
    

'''init: Initializes the scoreboard, sets the initial score to 0, and positions the scoreboard at the top of the screen.
    update_scoreboard: Clears the previous score and writes the current score on the screen.
    increase_score: Increases the score by 1 and updates the scoreboard.
    reset: Resets the score to 0 and updates the scoreboard.'''
class Scoreboard:
    def __init__(self):
        self.score = 0
        self.board = turtle.Turtle()
        self.board.color("white")
        self.board.penup()
        self.board.hideturtle()
        self.board.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.board.clear()
        self.board.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.update_scoreboard()



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
# Create the snake, snack, and scoreboard objects
snake = Snake()
snack = Snack()
scoreboard = Scoreboard()


# Keyboard bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


'''game_loop: The main game loop which handles snake movement, collision detection, and score updates. It:
    Changes the snake's direction.
    Moves the snake.
    Detects collision with the snack and grows the snake, refreshes the snack, and increases the score if the snake eats the snack.
    Detects collision with the wall and ends the game with a game-over message if the snake hits the wall.
    Detects collision with itself and ends the game with a game-over message if the snake hits itself.
    Updates the screen and sets a timer to call the game loop every 100 milliseconds.'''
# Function to start the game loop
def game_loop():
    snake.change_direction()
    snake.move()

    # Detect collision with snack
    if snake.head.distance(snack.snack) < 15:
        snack.refresh()
        snake.grow()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290 or snake.head.xcor() < -290 or
        snake.head.ycor() > 290 or snake.head.ycor() < -290
    ):
        messagebox.showinfo("Game Over", "You hit the wall! Game Over.")
        scoreboard.reset()
        screen.bye()

    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            messagebox.showinfo("Game Over", "You hit yourself! Game Over.")
            scoreboard.reset()
            screen.bye()

    screen.update()
    screen.ontimer(game_loop, 100)


'''show_start_message: 
    Displays a start message using tkinter's messagebox and starts the game loop after the user clicks OK.'''
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