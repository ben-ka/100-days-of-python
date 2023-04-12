from turtle import Turtle

class Score(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(pos)
    def game_over(self):
        self.home()
        self.write("game over",False,'center',('david',50,'bold'))
    def add_level(self):
        self.level+=1
        
