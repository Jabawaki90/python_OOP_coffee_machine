# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# def f():
#     timmy.forward(50)
#
# timmy.shape('turtle')
# timmy.color("red", "green")
# timmy.forward(15)
#
# my_screen.onkey(f, "Up")
# my_screen.listen()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu",  "Squirtle", "Charmander"])
table.add_column("Type", ["Electric",  "Water", "Fire"])
table.align["Pokemon Name"] = 'l'
table.align["Type"] = 'r'

print(table)
