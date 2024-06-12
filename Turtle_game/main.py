
import turtle
import random

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
