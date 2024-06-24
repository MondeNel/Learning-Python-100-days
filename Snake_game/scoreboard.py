import turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0  # Initialize the high score
        self.board = turtle.Turtle()
        self.board.color("white")
        self.board.penup()
        self.board.hideturtle()
        self.board.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current score and high score."""
        self.board.clear()
        self.board.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 22, "normal"))

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Reset the score to 0, update the high score if necessary, and update the scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
