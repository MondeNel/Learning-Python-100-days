import turtle
import tkinter as tk
from tkinter import messagebox
from snake import Snake
from snack import Snack
from scoreboard import Scoreboard

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the snake, snack, and scoreboard objects
snake = Snake()
snack = Snack()
scoreboard = Scoreboard()
snake_speed = 100  # Set the snake speed to a constant value

# Keyboard bindings
def set_keybindings():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

set_keybindings()

def reset_game():
    """Reset the game state for a new game."""
    global snake, snack, scoreboard
    snake.reset()
    snack.refresh()
    scoreboard.update_scoreboard()
    set_keybindings()
    game_loop()

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
        if messagebox.askyesno("Game Over", "You hit the wall! Do you want to play again?"):
            scoreboard.reset()
            reset_game()
        else:
            screen.bye()

    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            if messagebox.askyesno("Game Over", "You hit yourself! Do you want to play again?"):
                scoreboard.reset()
                reset_game()
            else:
                screen.bye()

    screen.update()
    screen.ontimer(game_loop, snake_speed)

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
