import random
card_num = ([2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"])
card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
num_random = random.choice(card_num)
suit_random = random.choice(card_suit)
print(num_random + suit_random)
from random import shuffle
x = [[i] for i in card_num]
shuffle(x)

