from turtle import Turtle, Screen
import random
moves = ["fd", "back", "right", "left"]
ben = Turtle()
ben.shape('triangle')

ben.speed(0)


# for _ in range(1000):
#     random_red = random.randint(0, 255) / 255
#     random_green = random.randint(0, 255) / 255
#     random_blue = random.randint(0, 255) / 255
#     ben.color(random_red, random_green, random_blue)
    
#     current_move = random.choice(moves)
#     if current_move in ["back", "fd"]:
#         getattr(ben, current_move)(50)
#     else:
#         getattr(ben, current_move)(90)
#         ben.forward(50)

for _ in range(120):
    random_red = random.randint(0, 255) / 255
    random_green = random.randint(0, 255) / 255
    random_blue = random.randint(0, 255) / 255
    ben.color(random_red, random_green, random_blue)
    ben.circle(100)
    ben.left(3)


   


















screen = Screen()
screen.exitonclick()
