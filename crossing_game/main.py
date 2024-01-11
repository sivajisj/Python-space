import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


player = Player()
# car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()
cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    #Detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            car_manager.out()
            game_is_on = False

    if(player.is_at_finish_line()):
        player.goto_start()
        scoreboard.increase_level()




screen.exitonclick()