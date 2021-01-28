from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, FONT
import time

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# init instances
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

# catch key events to control player movements
screen.listen()
screen.onkey(player.go_up, "Up")

# run game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with the car
    for car in car_manager.cars:
        if player.distance(car) < 30:
            annoucement = Turtle()
            annoucement.write(f"GAME OVER", align="center", font=FONT)

            game_is_on = False


    # detect successful crossing
    if player.is_at_finish_line():
        player.refresh_position()
        car_manager.increase_car_speed()
        score_board.update_scoreboard()


# exit game
screen.exitonclick()