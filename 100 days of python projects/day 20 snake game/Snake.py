from turtle import Turtle
class Snake:
    def __init__(self,amount_of_snakes) :
        self.all_turtles = []
        x = 0
        
        for i in range(amount_of_snakes):
            self.add_snake((x,0))     
            x -=20
            
    
    def add_snake(self, position):
        self.new_turtle = Turtle('square')
        self.new_turtle.penup()
        self.new_turtle.color('white')
        self.new_turtle.setposition(position)            
        self.all_turtles.append(self.new_turtle)

    def extend(self):
        self.add_snake((self.all_turtles[-1].xcor(),self.all_turtles[-1].ycor()))

    def move(self,all_turtles):
        for turtle in range(len(all_turtles)-1,-1,-1):       
            if turtle==0:
                all_turtles[0].forward(20)
                
                    
            else:
                all_turtles[turtle].goto(all_turtles[turtle-1].pos())   
    def up(self):
        if self.all_turtles[0].heading() != 270:
            self.all_turtles[0].setheading(90)
    def right(self):
        if self.all_turtles[0].heading() != 180:
            self.all_turtles[0].setheading(0)
    def left(self):
        if self.all_turtles[0].heading() != 0:
            self.all_turtles[0].setheading(180)
    def down(self):
        if self.all_turtles[0].heading() != 90:
            self.all_turtles[0].setheading(270)

