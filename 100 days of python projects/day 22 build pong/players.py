from turtle import Turtle

MOVEMENT_SPEED = 30
class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=6,stretch_len=1)
        self.goto(position) 
        self.color('white')
        

    def up(self):
        self.sety(self.ycor()+MOVEMENT_SPEED)
    def down(self):
        
        self.sety(self.ycor()-MOVEMENT_SPEED)






