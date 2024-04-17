#Challenge 1 - Picking a Random Words and Checking Answers

import random

word_list = ["ardvark", "baboon", "camel"]
list_random = random.choice(word_list)
word_lenght = len(list_random)

display = []
for _ in range(len(list_random)):
        display += "_"

end_of_game = False

while not end_of_game:

    Letter = (input("Digite anything letter ")).lower()

    for position in range(0, word_lenght):
        letters = list_random[position]

        if letters == Letter:  
            display[position] = Letter  
            
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")

#Challenge 2 - Replacing Blanks with Guesses

#Challenge 3 = Checking if the Player has Won


