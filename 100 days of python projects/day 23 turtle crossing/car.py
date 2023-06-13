from turtle import Turtle
from random import randint
import time
BASE_SPEED = 60
class Car(Turtle):
    def __init__(self,pos,min):
        super().__init__()
        self.penup()
        self.r = randint(0,200)/255
        self.g = randint(0,200)/255
        self.b = randint(0,200)/255
        self.color((self.r,self.g,self.b))
        self.shape('square')
        self.goto(pos)
        self.shapesize(1,3)
        self.seth(180)
        self.min_x = min
        self.did_reach = False
        self.speed = BASE_SPEED
    def move(self):
        time.sleep(0.03)
        self.forward(self.speed)
    def check_if_crossed(self):
        if self.xcor() < self.min_x:
            return True
        return False

    


        
