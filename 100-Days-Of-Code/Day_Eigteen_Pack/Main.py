from turtle import Turtle, Screen
import random

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

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
t.screen.bgcolor("Black")

"""
def draw_shape(sides):

    angle = 360 / sides
    random_color = random.choice(colours)
    for ang in range(sides):
        t.color(random_color)
        t.forward(100)
        t.right(angle)
    
    sides += 1

for shape_Side_n in range(3, 11):
    draw_shape(shape_Side_n)
"""
Position = [90, 180 , 270 , 360]
def Forward_turtle():
    t.pensize(5)
    t.speed(10)
    for ang in range(100):
        t.color(random.choice(colours))
        t.forward(20)
        t.left(random.choice(Position))
        
    
        

Forward_turtle()


screen = Screen()
screen.exitonclick()