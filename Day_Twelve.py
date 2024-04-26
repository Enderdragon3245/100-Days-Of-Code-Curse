#Namespaces: Local vs. Global Scope
from random import randint

 
EASY_LEVEL = 10
HARD_LEVEL = 5

def difficulty_return(guess , answer):
    if guess > ansyer:
        print("Too High")
    elif guess < ansyer:
        print("Too Low")
    else:
        print(f"You got it! The  answer is {ansyer}")
    
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty == "easy":
       return turns = EASY_LEVEL
    else:
       return turns = HARD_LEVEL



print("Welcome to the Nubmer Guessing Game!")
print("I'm thinking of a number between 1 and 100")
ansyer = randint(1, 100)


guess = int(input("Make a Guess"))
turns = set_difficulty()
print(f"You Have {turns} attmpts remaining")




    




