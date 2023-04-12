from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.home()
        self.color('white')
        self.x = 7
        self.y = 10
    def go_to_start(self):      
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)

    def bounce_with_wall(self):
        self.y = self.y * (-1)
    def bounce_with_player(self):
        
        self.x = self.x * (-1)
      
       

    
        
