#Functions 
import math

def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the weather nice today?")

greet()

#Functions that allows for input

def greet_with_name(name):
    print(f"How wo doin {name}?")

greet_with_name("gustavo")

def greet_with(name, location):
    print(f"Hello {name}, what is it like in {location}")

greet_with("Gustavo", "Russas") #Position Argument = Default
greet_with(name="Gustavo", location="Russas") #Keyword Arguments

#Challenge 1 Calculating the area of ​​a wall


def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  
  print(f"You'll need {round_up_cans} cans of paint.")


test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)