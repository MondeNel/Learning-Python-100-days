import turtle
import random

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
