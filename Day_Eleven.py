import random

your_cards = []
Computer_cards = []
current_score = 0

def deal_card():
    cards = [11, 2, 3, 4, 5, 6 , 7 ,8 ,9 ,10 ,10 ,10 ,10]
    card = random.choice(cards)
    return card

for _ in range(2):
    your_cards.append(deal_card())
    Computer_cards.append(deal_card())

for _ in range(0 , len(your_cards)):
    current_score += your_cards[_]


if current_score > 21:
    print("Your Lost, Computer Win's")

print(f"Your cards: {your_cards}, current score: {current_score}")
print(f"Computer's first card: {Computer_cards[0]}")








#Blackjack Program Requirements and Game Rules
