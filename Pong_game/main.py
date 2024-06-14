import turtle

'''screen.title: Sets the title of the window.
    screen.bgcolor: Sets the background color of the screen to black.
    screen.setup: Sets the screen size to 800x600 pixels.
    screen.tracer: Turns off automatic screen updates to control when the screen updates.'''
# Set up the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
