import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.step, 'Up')
game_is_on = True
all_cars = CarManager()
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    all_cars.traffic()
    scoreboard.display_level()
    for car in all_cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.crossed_finish_line():
        player.move_to_start()
        all_cars.increase_difficulty()
        scoreboard.level_up()
    time.sleep(0.1)

screen.exitonclick()


