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




def draw_shape(sides):

    angle = 360 / sides

    for ang in range(sides):
        t.forward(100)
        t.right(angle)
    
    sides += 1

for shape_Side_n in range(3, 11):
    draw_shape(shape_Side_n)


screen = Screen()
screen.exitonclick()