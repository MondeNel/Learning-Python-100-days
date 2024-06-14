import turtle

'''screen.title: Sets the title of the window.
    screen.bgcolor: Sets the background color of the screen to black.
    screen.setup: Sets the screen size to 800x600 pixels.
    screen.tracer: Turns off automatic screen updates to control when the screen updates.'''
# Step 1: Set Up the Screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# Step 2: Create the Paddle Class
'''init: Initializes the paddle with a specific position and sets its shape, color, and size.
    go_up: Moves the paddle up by 20 pixels, ensuring it stays within the screen bounds.
    go_down: Moves the paddle down by 20 pixels, ensuring it stays within the screen bounds.'''

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
'''init: Initializes the ball, sets its shape, color, and initial movement direction.
    move: Moves the ball in its current direction.
    bounce_y: Reverses the ball's y-direction when it hits the top or bottom walls.
    bounce_x: Reverses the ball's x-direction when it hits a paddle.
    reset_position: Resets the ball to the center and reverses its x-direction after a point is scored.'''

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
