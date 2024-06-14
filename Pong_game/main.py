import turtle

''' * screen.title: Sets the title of the window.
    * screen.bgcolor: Sets the background color of the screen to black.
    * screen.setup: Sets the screen size to 800x600 pixels.
    * screen.tracer: Turns off automatic screen updates to control when the screen updates.'''
# Step 1: Set Up the Screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# Step 2: Create the Paddle Class
''' * init: Initializes the paddle with a specific position and sets its shape, color, and size.
    * go_up: Moves the paddle up by 20 pixels, ensuring it stays within the screen bounds.
    * go_down: Moves the paddle down by 20 pixels, ensuring it stays within the screen bounds.'''

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




# Step 3: Create the Ball Class
''' * init: Initializes the ball, sets its shape, color, and initial movement direction.
    * move: Moves the ball in its current direction.
    * bounce_y: Reverses the ball's y-direction when it hits the top or bottom walls.
    * bounce_x: Reverses the ball's x-direction when it hits a paddle.
    * reset_position: Resets the ball to the center and reverses its x-direction after a point is scored.'''

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


# Step 4: Create the Scoreboard Class
''' * init: Initializes the scoreboard, sets its color, hides the turtle, and initializes scores for both players.
    * update_score: Clears the previous score and writes the current score on the screen.
    * l_point: Increases the left player's score by 1 and updates the scoreboard.
    * r_point: Increases the right player's score by 1 and updates the scoreboard.'''

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


# Step 5: Set Up the Game Logic
''' * left_paddle: Creates the left paddle at the specified position.
    * right_paddle: Creates the right paddle at the specified position.
    * ball: Creates the ball object.
    * scoreboard: Creates the scoreboard object.
    * screen.listen: Sets the screen to listen for key presses.
    * screen.onkey: Binds the keys to the paddle movements.
    * while True: The main game loop that continuously updates the screen, moves the ball, 
        detects collisions with the walls and paddles, and updates the score.'''

# Create paddles
left_paddle = Paddle(-350)
right_paddle = Paddle(350)

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# Main game loop
while True:
    screen.update()
    ball.move()

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
