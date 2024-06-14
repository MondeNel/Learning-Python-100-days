import turtle
import tkinter as tk
from tkinter import messagebox

# Set up the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

class Paddle(turtle.Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -240:
            self.goto(self.xcor(), new_y)

    def track_ball(self, ball_y):
        if self.ycor() < ball_y:
            self.go_up()
        elif self.ycor() > ball_y:
            self.go_down()

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 24, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 24, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

# Create paddles
left_paddle = Paddle(-350)
right_paddle = Paddle(350)

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")

# Function to start the game loop
def game_loop():
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

    # Move the computer paddle to track the ball
    right_paddle.track_ball(ball.ycor())

    # Set the timer to call game_loop again after 20 milliseconds
    screen.ontimer(game_loop, 20)

# Function to show start message
def show_start_message():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Pong Game", "Click OK to start the game.")
    root.destroy()
    # Start the game loop after the user clicks OK
    game_loop()

# Show the start message and then start the game
show_start_message()

# Keep the window open
screen.mainloop()
