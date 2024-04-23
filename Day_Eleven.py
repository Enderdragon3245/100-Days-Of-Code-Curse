import random

your_cards = []
Computer_cards = []
is_game_over = False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6 , 7 ,8 ,9 ,10 ,10 ,10 ,10]
    card = random.choice(cards)
    return card

def calculed_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

for _ in range(2):
    your_cards.append(deal_card())
    Computer_cards.append(deal_card())

user_score = calculed_score(your_cards)
Computer_score = calculed_score(Computer_cards)

print(f"Your cards: {your_cards}, current score: {user_score}")
print(f"Computer's first card: {Computer_cards[0]}")



if user_score == 0 or Computer_score == 0 or user_score > 21:
    is_game_over = True













#Blackjack Program Requirements and Game Rules
