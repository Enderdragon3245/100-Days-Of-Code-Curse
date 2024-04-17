#Challenge 1 - Picking a Random Words and Checking Answers

import random

word_list = ["ardvark", "baboon", "camel"]
list_random = random.choice(word_list)
word_lenght = len(list_random)

display = []
for _ in range(len(list_random)):
        display += "_"

end_of_game = False
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

while not end_of_game:

    Guess = (input("Digite anything letter ")).lower()

    for position in range(0, word_lenght):
        letters = list_random[position]

        if letters == Guess:  
            display[position] = letters
         
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    if Guess not in list_random:
        lives -= 1
        print(stages[lives])
        
        if lives == 0:
            end_of_game = True
            print("Game Over")

#Challenge 2 - Replacing Blanks with Guesses

#Challenge 3 - Checking if the Player has Won

#Challenge 4 - Keeping Track of the Player's Lives


