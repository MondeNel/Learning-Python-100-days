import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up keyboard bindings
screen.listen()
screen.onkey(player.move_up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Check if player has reached the finish line
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

# Keep the window open
screen.mainloop()
