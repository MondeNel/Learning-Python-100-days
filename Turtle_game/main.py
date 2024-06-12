
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


# Create the racing turtles
colors = ["red", "blue", "green", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50]
turtles = []

for i in range(5):
    turtles.append(RacingTurtle(colors[i], y_positions[i]))

# User-controlled turtle
user_turtle = turtles[0]

# Draw the starting and finishing lines
start_line = turtle.Turtle()
start_line.penup()
start_line.goto(-250, -100)
start_line.pendown()
start_line.goto(-250, 100)
start_line.hideturtle()

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(230, -100)
finish_line.pendown()
finish_line.goto(230, 100)
finish_line.hideturtle()

# Bind the space key to the user-controlled turtle
screen.listen()
screen.onkey(user_move, "space")

# Start the race
race_on = True

while race_on:
    for racing_turtle in turtles:
        if racing_turtle != user_turtle:
            racing_turtle.move_forward()
        
        # Check if any turtle has crossed the finish line
        if racing_turtle.get_x_position() >= 230:
            race_on = False
            winner_color = racing_turtle.turtle.pencolor()
            print(f"The winner is the {winner_color} turtle!")
            break

screen.mainloop()