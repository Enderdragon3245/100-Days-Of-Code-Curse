#Blackjack Program Requirements and Game Rules
import random

cards = [11, 2, 3, 4, 5, 6 , 7 ,8 ,9 ,10 ,10 ,10 ,10]
Play = input("You wanna play Black Jack? 'yes' or 'no' ")

Should_Play = None
if Play == "yes":
    Should_Play = True
else:
    Should_Play = False

your_cards = [None, None]
Computer_cards = [None, None]
def black_Jack(f_cards):

    your_cards[0] = random.choice(f_cards)
    your_cards[1] = random.choice(f_cards)
    current_score = your_cards[0] + your_cards[1]
    print(f"Your cards: {your_cards}, current score: {current_score}")

    Computer_cards[0] = random.choice(f_cards)
    Computer_cards[1] = random.choice(f_cards)
    print(f"Computer's first card: {Computer_cards[0]}")


black_Jack(cards)
