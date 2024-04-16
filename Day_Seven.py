#Challenge 1 - Picking a Random Words and Checking Answers

import random

word_list = ["ardvark", "baboon", "camel"]
list_random = random.choice(word_list)

Letter = str(input("Digite anything letter ")).lower()
print(list_random)


for letters in list_random:
    if Letter == letters:
        print("yes")
    else:
        print("No")