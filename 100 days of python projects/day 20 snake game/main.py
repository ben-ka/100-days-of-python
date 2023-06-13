from turtle import Turtle,Screen
import time
from Snake import Snake
from food import Food
from score import Score
import random

WIDTH = 900
HEIGHT = 900
random_x = random.randint(-WIDTH/2+WIDTH/10,WIDTH/2 -WIDTH/10)
random_y = random.randint(-HEIGHT/2+HEIGHT/10, HEIGHT/2 -HEIGHT/10)
screen = Screen()

screen.setup(WIDTH,HEIGHT)
screen.bgcolor('black')
screen.title('snake')
screen.tracer(0)
amount_of_snakes = 3
snake = Snake(amount_of_snakes)
food = Food(random_x,random_y)
my_score = Score(0, HEIGHT / 2 - HEIGHT/12)

def listen():
    screen.listen()
    screen.onkey(snake.right,'Right')
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.down,"Down")

def snake_in_bounds():
    if (snake.all_turtles[0].xcor() > WIDTH/2) or snake.all_turtles[0].xcor() < -WIDTH/2:
        return False
    if snake.all_turtles[0].ycor() > HEIGHT /2 or snake.all_turtles[0].ycor() < -HEIGHT/2:
        return False
    return True

def collision_with_food():
    if snake.all_turtles[0].distance(food) <20:
        return True     
    return False

def collision_with_tail():
    for i in range(1,len(snake.all_turtles)):
        if snake.all_turtles[0].xcor() > snake.all_turtles[i].xcor() - 10 and snake.all_turtles[0].xcor() < snake.all_turtles[i].xcor() + 10 :
            if snake.all_turtles[0].ycor() > snake.all_turtles[i].ycor() - 10 and snake.all_turtles[0].ycor() < snake.all_turtles[i].ycor() + 10:
                return True
    return False


game_is_on =True
while game_is_on:
    
    screen.update()
    time.sleep(0.06)
    
    listen()
    if collision_with_tail() ==True:
        my_score.reset_score()
        snake.reset_game()
        snake.all_turtles[0].home()
    snake.move(snake.all_turtles)
    if snake_in_bounds() == False:  
        snake.all_turtles[0].home()        # detect collision with walls
        my_score.reset_score()
        snake.reset_game()
    if collision_with_food() ==True:
        my_score.add_score()
        my_score.clear()
        food.hideturtle()
        snake.extend()
        random_x = random.randint(-WIDTH/2+WIDTH/10,WIDTH/2 -WIDTH/10)
        random_y = random.randint(-HEIGHT/2+HEIGHT/10, HEIGHT/2 -HEIGHT/10)
        food = Food(random_x,random_y)
    my_score.update_score()
    #detect collision with tail
    





snake.all_turtles[0].setpos(-WIDTH/7,0)
#snake.all_turtles[0].write('game over',False,'left',('courier',35,'bold'))   

    

 

        
            
            
            

          


screen.exitonclick()