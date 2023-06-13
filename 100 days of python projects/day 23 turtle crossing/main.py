from turtle import Turtle, Screen
import time
from turtle_behavior import TurtleBehavior
from car import Car
import random
from score import Score

WIDTH = 1200
HEIGHT = 900

all_cars =  []

screen = Screen()
screen.tracer(0)
screen.setup(WIDTH,HEIGHT)

ben = TurtleBehavior((0,-WIDTH/4))

def listen_to_moves():
    screen.listen()
    screen.onkey(ben.move,"Up")

def detect_collision_with_car(car):
        if car.xcor() <=0 and ben.distance(car) < 7:
            return True
        return False

def check_if_pass_level():
    if ben.ycor() > HEIGHT/2:
        
        return True
    return False

score = Score((-WIDTH/2 + WIDTH/7,HEIGHT/2 - HEIGHT/7))



game_is_on = True
while game_is_on:
    score.write(f'level: {score.level}',False,'left',('david',30,'normal'))
    screen.update()
    time.sleep(0.05)
    new_car = Car((WIDTH/2,random.randint(-WIDTH/2,WIDTH/2)),-WIDTH/2)
    all_cars.append(new_car)
    for car in all_cars:
        car.move()
        if car.check_if_crossed():
            car.reset()
            car.hideturtle()
            all_cars.remove(car)
        if detect_collision_with_car(car):
            game_is_on = False
    
    if check_if_pass_level():
        score.reset()
        score.penup()
        score.hideturtle()
        score.goto(-WIDTH/2 + WIDTH/7,HEIGHT/2 - HEIGHT/7)
        score.add_level()
        ben.goto(0,-WIDTH/4)
        for car in all_cars:
            car.speed *=1.5  


    listen_to_moves()
    
score.game_over()








screen.exitonclick()