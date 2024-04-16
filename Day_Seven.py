#Challenge 1 - Picking a Random Words and Checking Answers

import random

word_list = ["ardvark", "baboon", "camel"]
list_random = random.choice(word_list)

Letter = str(input("Digite anything letter"))
print(list_random)


for word in word_list:
    if word == list_random:

        for letters in word:
            if Letter == letters:
                print("Yes")
            else:
                print("No")