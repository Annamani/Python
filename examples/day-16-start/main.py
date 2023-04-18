# ## above or the below one are same
# #from turtle import Turtle
# #timmy=Turtle()
# #print(timmy)
#
# import turtle
# timmy=turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen= turtle.Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()
#
#
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.add_column("Count",["200","100","9"])

table.align="r"
print(table)