from turtle import Turtle
class Score(Turtle):
    def __init__(self , xpos ,ypos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.setpos(xpos,ypos)
    def add_score(self):
        self.score+=1
        