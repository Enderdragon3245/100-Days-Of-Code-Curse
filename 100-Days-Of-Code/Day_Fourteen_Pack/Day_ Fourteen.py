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
    

Compareted_Number = randint(0, 15)
Compare_A(Compareted_Number)