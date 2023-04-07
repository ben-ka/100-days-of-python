# import colorgram

# colors = []
# format_colors = []
# colors += colorgram.extract('hirst-painting\image.jpg',72)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new = (r,g,b)
#     format_colors.append(new)
     
# print(format_colors)

color_list = [ (202, 163, 98), (45, 97, 147), (168, 49, 80), (222, 210, 108), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (100, 50, 42), (34, 61, 117), (223, 208, 22), (148, 207, 225), (169, 187, 225), (233, 173, 163), (49, 57, 66), (41, 75, 78), (74, 47, 41), (24, 91, 88), (85, 32, 52), (30, 62, 61)]

import turtle
turtle.colormode(255)
from random import choice
ben = turtle.Turtle()

ben.shape('triangle')
ben.hideturtle()
ben.speed(0)
ben.penup()
ben.setposition(-320,-300)

for i in range(10):
    for j in range(9):
        ben.color(choice(color_list))
        ben.dot(20)
        ben.forward(70)
    if i % 2 == 0:
        ben.dot(20)
        ben.left(90)
        ben.forward(50)
        ben.left(90)
    else:
        ben.dot(20)
        ben.right(90)       
        ben.forward(50)
        ben.right(90)



screen = turtle.Screen()
screen.exitonclick()