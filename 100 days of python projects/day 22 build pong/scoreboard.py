from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color('white')
        self.score = 0
        self.hideturtle()
    def add_score(self):
        self.score+=1

