from turtle import Turtle
LINE_LENGTH =50
GAP_BETWEEN = 20
AMOUNT_OF_LINES = 20
class Border(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.seth(90)
        self.color('white')
        for i in range(AMOUNT_OF_LINES):
            self.pendown()
            self.pensize(width=5)
            self.forward(LINE_LENGTH)
            self.penup()
            self.forward(GAP_BETWEEN)


    
