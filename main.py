from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
def f():
    timmy.forward(50)

timmy.shape('turtle')
timmy.color("red", "green")
timmy.forward(15)

my_screen.onkey(f, "Up")
my_screen.listen()

my_screen.exitonclick()