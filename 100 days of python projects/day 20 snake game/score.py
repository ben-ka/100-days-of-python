from turtle import Turtle

class Score(Turtle):
    
    def __init__(self , xpos ,ypos):
       
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        with open('high_scores.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.setpos(xpos,ypos)
    def add_score(self):
        self.score+=1
    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}  high score: {self.high_score}',False,'center',('courier',26,'bold'))
    def reset_score(self):
        
        if self.score > self.high_score:
            with open('high_scores.txt','w') as file:
                file.write(str(self.score))
            with open('high_scores.txt') as file:
                self.high_score = int(file.read())
        else:
            with open('high_scores.txt','w') as file:
                file.write(str(self.high_score))
        self.score = 0 
        self.update_score()

        