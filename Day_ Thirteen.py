#Debugging: How to Find and Fix

#Describe the Problem

def my_function():
    for i in range(1, 21): #This here goes from number 1 to number 19 --The Problem
        if i == 20:
            print("You got it")
my_function()

#The problem here is the print is not work

#Reproducing the bug

from random import randint
dice_imgs = ["1", "2","3","4","5","6"] #A list from the index 0 until 5
dice_num = randint(0 , 5) #This select a number from the number 1 until 6
print(dice_imgs[dice_num])