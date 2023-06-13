from turtle import Screen, Turtle
from players import Player
from border import Border
from scoreboard import ScoreBoard
from ball import Ball
import time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

MARGIN_OFF_WALLS = 30

screen = Screen()
screen.tracer(0)
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.bgcolor('black')

score_left = ScoreBoard((-SCREEN_WIDTH/10,SCREEN_HEIGHT/2 - SCREEN_HEIGHT/10))
score_right = ScoreBoard((SCREEN_WIDTH/10,SCREEN_HEIGHT/2 - SCREEN_HEIGHT/10))

player1 = Player((-SCREEN_WIDTH/2 + SCREEN_WIDTH/40 ,0))
player2 = Player((SCREEN_WIDTH/2 -SCREEN_WIDTH/40 ,0))

border = Border((0,-SCREEN_HEIGHT/2))

ball = Ball()

def handle_movement():
    screen.listen()
    screen.onkey(player1.up,"w",)
    screen.onkey(player2.up,"Up")
    screen.onkey(player1.down,"s")
    screen.onkey(player2.down,"Down")

def handle_with_screen_borders():
    if player1.ycor() > SCREEN_HEIGHT/2 - 30:
        player1.sety(SCREEN_HEIGHT/2 - 30)
    if player1.ycor() < -SCREEN_HEIGHT/2 + 30:
        player1.sety(-SCREEN_HEIGHT/2 + 30)

    if player2.ycor() > SCREEN_HEIGHT/2 - 30:
        player2.sety(SCREEN_HEIGHT/2 - 30)
    if player2.ycor() < -SCREEN_HEIGHT/2 + 30:
        player2.sety(-SCREEN_HEIGHT/2 + 30)

def handle_with_bounces_with_wall():
    if ball.ycor() > SCREEN_HEIGHT/2 - MARGIN_OFF_WALLS:
        ball.bounce_with_wall()
        return True

    if ball.ycor() < -SCREEN_HEIGHT/2 + MARGIN_OFF_WALLS:
        ball.bounce_with_wall()
        return True
    return False

def detect_collisions_with_player():
    if ball.xcor() < SCREEN_WIDTH/2 -SCREEN_WIDTH/40  and ball.distance(player2) < 30:
        ball.bounce_with_player()
    
    if ball.xcor() > -SCREEN_WIDTH/2  + SCREEN_WIDTH/40  and ball.distance(player1) < 30:
        ball.bounce_with_player()
    
    


round_is_on = True

while round_is_on:
    score_left.write(f'{score_left.score}',False,'center',('courier',50,'bold'))
    score_right.write(f'{score_right.score}',False,'center',('courier',50,'bold'))
    time.sleep(0.04)
    screen.update()
    
    ball.go_to_start()
    handle_with_bounces_with_wall()
    detect_collisions_with_player()
    handle_movement()
    handle_with_screen_borders()




screen.exitonclick()