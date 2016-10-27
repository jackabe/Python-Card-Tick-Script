import random
card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
deck = []

#make a deck first and then choose 21 from there.
for i in range (len(card_value)): #this will create a deck of 52 cards
    deck.append(card_value[i]+ " of " + card_suit[0])
    deck.append(card_value[i]+ " of " + card_suit[1])
    deck.append(card_value[i]+ " of " + card_suit[2])
    deck.append(card_value[i]+ " of " + card_suit[3])


random.shuffle(deck) #that'll shuffle your 52 cards

cards_21 = []
#now create 21.
for i in range(0,21): #first 21 from then shuffled deck gets added
    cards_21.append(deck[i])
    deck.pop(i)

print("--------------------------------------")

list_one = []
list_two = []
list_three = []

print("Welcome to the game, here I will make you choose a random card out of 21. I will then guess it for you")
print("I will deal 21 cards in 3 columns, pick a card in a column and tell me which one it is in")

print("--------------------------------------")

for i in range(0,7):
    list_one.append(cards_21[i])
for i in range(7,14):
    list_two.append(cards_21[i])
for i in range(14,21):
    list_three.append(cards_21[i])

print("Column one: {0}".format(list_one))
print("--------------------------------------")
print("Column two: {0}".format(list_two))
print("--------------------------------------")
print("Column three: {0}".format(list_three))

user_column = input("Which column is your card in?: ")
user_column = int(user_column)
print("--------------------------------------")
print("You have chosen column {0}".format(user_column))
print("--------------------------------------")

cards_21 = []

if user_column == 1:
    for i in range(0,7):
        cards_21.append(list_two[i])
    for i in range(0,7):
        cards_21.append(list_one[i])
    for i in range(0,7):
        cards_21.append(list_three[i])

if user_column == 2:
    for i in range(0,7):
        cards_21.append(list_one[i])
    for i in range(0,7):
        cards_21.append(list_two[i])
    for i in range(0,7):
        cards_21.append(list_three[i])

if user_column == 3:
    for i in range(0,7):
        cards_21.append(list_one[i])
    for i in range(0,7):
        cards_21.append(list_three[i])
    for i in range(0,7):
        cards_21.append(list_two[i])

list_one = []
list_two = []
list_three = []

for i in range(0,7):
    list_one.append(cards_21[i])
for i in range(7,14):
    list_two.append(cards_21[i])
for i in range(14,21):
    list_three.append(cards_21[i])

print("Column one: {0}".format(list_one))
print("--------------------------------------")
print("Column two: {0}".format(list_two))
print("--------------------------------------")
print("Column three: {0}".format(list_three))

user_column = input("Which column is your card in?: ")
user_column = int(user_column)
print("--------------------------------------")
print("You have chosen column {0}".format(user_column))
print("--------------------------------------")


print("--------------------------------------")
user_column = input("I have now re dealt the cards. Which column is it in now?: ")
