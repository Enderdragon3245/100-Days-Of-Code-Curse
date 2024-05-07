from turtle import Turtle, Screen


t = Turtle()
"""
t2 = Turtle()
t2.color("red")

for ang in range(0, 4):
    t.forward(100)
    t.left(90)
    t2.left(90)
    t2.forward(100)

for ang in range(0 , 10):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)

"""
sides = 3
angle = 360
is_on = True


while is_on:
    for ang in range(0 , sides):
        result = angle / sides
        t.forward(100)
        t.right(result)
    
    sides += 1

    

screen = Screen()
screen.exitonclick()