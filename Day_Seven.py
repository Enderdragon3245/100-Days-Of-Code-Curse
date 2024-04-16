#Challenge 1 - Picking a Random Words and Checking Answers

import random

word_list = ["ardvark", "baboon", "camel"]
list_random = random.choice(word_list)

Letter = str(input("Digite anything letter ")).lower()
print(list_random)


display = []
for _ in range(len(list_random)):
    display += "_"

for position in range(len(list_random)):
    letters = list_random[position]
    if Letter == letters:
        print("yes")      
        display[position] = Letter  
    else:
        print("No")

print(display)

#Challenge 2 - Replacing Blanks with Guesses


