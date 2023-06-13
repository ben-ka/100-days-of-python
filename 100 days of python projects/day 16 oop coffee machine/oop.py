# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.hideturtle()
# timmy.shape("turtle")
# timmy.color('coral')
# timmy.fd(100)



# my_screen = Screen()


# print(my_screen)

# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name",["pikachu", "squirtle","charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align["Pokemon name"] = 'l'
table.align['Type'] ='c'
print(table.align)
print(table)







