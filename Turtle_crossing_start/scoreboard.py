from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """Class to manage the game scoreboard."""
    
    def __init__(self):
        """Initialize the scoreboard with a level counter and display it."""
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level by 1 and update the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display 'GAME OVER' at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
