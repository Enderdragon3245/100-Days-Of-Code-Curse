#Namespaces: Local vs. Global Scope
import random

 
should_continue = True
attempts = 0
ansyer = []
for i in range(1, 101):
    ansyer.append(i)

thinking_number = random.choice(ansyer)
print(thinking_number)

print("Welcome to the Nubmer Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def difficulty_choice():
    global attempts
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5    
    return attempts   
attempts_choice = difficulty_choice()

def difficulty_return(guess_choice):
    if guess_choice == thinking_number:
        print("You Guess Right!!!")
        should_continue = False
        return should_continue
    elif guess_choice > thinking_number:
        print("Too High")
        print("Guess again")
        attempts_choice - 1
    else:
        print("Too low")
        print("Guess again")
        attempts_choice - 1
    
  





while should_continue:
    print(f"You have {attempts_choice} attempts remaining to guesse the number")
    guess = int(input("Make a guess: "))

    difficulty_return(guess)



