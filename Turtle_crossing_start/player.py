from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """Class to represent the player-controlled turtle."""
    
    def __init__(self):
        """Initialize the player at the starting position."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def goto_start(self):
        """Place the player turtle at the starting position."""
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Move the player turtle up by the MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        """Check if the player has reached the finish line."""
        return self.ycor() > FINISH_LINE_Y
