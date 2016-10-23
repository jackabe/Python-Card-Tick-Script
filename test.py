import random
card_type = (["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"])
card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
card_random = random.choice(card_type)
suit_random = random.choice(card_suit)
card = (card_random + " of " + suit_random)

user_input = input("Would you like a card?: ")
if user_input == "yes":
    print(card)

