#Debugging: How to Find and Fix

#Describe the Problem

def my_function():
    for i in range(1, 21): #This here goes from number 1 to number 19 --The Problem
        if i == 20:
            print("You got it")
my_function()

#The problem here is the print is not work
#Solution: change 20 in 21 range

#Reproducing the bug

from random import randint
dice_imgs = ["1", "2","3","4","5","6"] #A list from the index 0 until 5
dice_num = randint(0 , 5) #This select a number from the number 1 until 6
print(dice_imgs[dice_num])

#Solution: Change 1,6 for 0,5
#Play Computer and Evaluate Each Line

year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994: #This code excludes the possibility of the year being 1994
    print("You are a millenial")
elif year > 1994:  #no if state or elif checks the year 1994
    print("You are a Gen Z.")
#Solution: =