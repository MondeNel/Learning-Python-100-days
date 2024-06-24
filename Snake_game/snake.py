import turtle

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
