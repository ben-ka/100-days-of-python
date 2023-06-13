from turtle import Turtle

class Food(Turtle):
    def __init__(self, random_spot_x,random_spot_y):
        super().__init__()
        self.speed(0)
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('blue')       
        self.goto(random_spot_x,random_spot_y)
        
        

        