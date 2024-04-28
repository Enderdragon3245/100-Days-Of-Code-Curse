#Introduction & Program Requirements for the Higher Lower Game
from random import randint
from Art import logo
from Game_Data import data
#Create a mini DB for Compareted 
print(logo)

#Def Compare
def Compare_A(Number):
    Compare_name = data[Number]["name"]
    Compare_Description = data[Number]["description"]
    Compare_County = data[Number]["country"]
    Compare_follower_count = data[Number]["follower_count"]

    print(f"Compare A: {Compare_name}, {Compare_Description}, from {Compare_County}")

#Remove equals Compareteds in Game.
def Remove_equals(Number, Number2):
    global Compareted_Number_B

    while Number == Number2:
        Compareted_Change = randint(0, 15)
        Compareted_Number_B = Compareted_Change
        return Compareted_Number_B
        


Compareted_Number_A = randint(0, 5)
Compareted_Number_B = randint(0, 5)

Compare_A(Compareted_Number_A)
Compare_A(Compareted_Number_B)
Remove_equals(Compareted_Number_A, Compareted_Number_B)
print(Compareted_Number_B)