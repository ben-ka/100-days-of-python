from turtle import Turtle,Screen
from random import randint
COLORS = ["red","orange","yellow","green","blue","purple"]
WIDTH = 1000
HEIGHT =700
starting_height = -100
is_race_on =False

screen = Screen()
screen.setup(WIDTH,HEIGHT)
all_turtles = []

user_bet = screen.textinput("Make your bet","which turtle will win the race. enter a color? ")
for color in COLORS:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-WIDTH/2+15,starting_height)
    all_turtles.append(new_turtle)
    starting_height+=50


if user_bet in COLORS and user_bet:
    is_race_on =True

i= 0
while is_race_on:
    random_speed = randint(5,20)
    all_turtles[i].forward(random_speed)
    if all_turtles[i].xcor() >= WIDTH/2 -20 :
        winner = all_turtles[i]
        winner_color = (winner.color()[0])
        break
    
    if i < len(all_turtles) - 1:
        i+=1
    else:
        i = 0
if user_bet ==winner_color:
    print(f"you won. the winner is {winner_color}")
else:
    print(f"you lost. the winner is {winner_color} ")
    
    










screen.exitonclick()
