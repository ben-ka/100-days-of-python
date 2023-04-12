from turtle import Turtle

MOVE_LENGTH = 35
class TurtleBehavior(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.move_length = MOVE_LENGTH
        self.shape('turtle')
        self.setheading(90)
        self.goto(pos)
        self.shapesize(1.5,1.5)
    
    def move(self):
        self.forward(self.move_length)
