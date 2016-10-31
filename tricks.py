import random

def welcome_text():
    print("Welcome to the game. Please choose a card and I will try to guess it.")
    print("I will deal 21 cards in 3 columns. Pick a card in a column and tell me which one it is in")
    print("-----------------------------------------------------")

def create_shuffled_deck():
    card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
    global deck
    deck = []
    for i in range (len(card_value)):
        deck.append(card_value[i]+ " of " + card_suit[0])
        deck.append(card_value[i]+ " of " + card_suit[1])
        deck.append(card_value[i]+ " of " + card_suit[2])
        deck.append(card_value[i]+ " of " + card_suit[3])
        random.shuffle(deck)

def take_21_cards():
    global cards_21
    cards_21 = []
    for i in range(0,21):
        cards_21.append(deck[i])
        deck.pop(i)

welcome_text()
create_shuffled_deck()
take_21_cards()

def user_choose():
    print("--------------------------------------")
    print("Column one: {0}".format(list_one))
    print("--------------------------------------")
    print("Column two: {0}".format(list_two))
    print("--------------------------------------")
    print("Column three: {0}".format(list_three))
    print("--------------------------------------")
    global user_column
    user_column = input("Which column is your card in?: ")
    user_column = int(user_column)
    print("--------------------------------------")
    print("You have chosen column {0}".format(user_column))
    print("--------------------------------------")

list_one = []
list_two = []
list_three = []
for i, card in enumerate(cards_21):
    if i%3 == 0:
        list_one.append(cards_21[i])
    if i%3 == 1:
        list_two.append(cards_21[i])
    if i%3 == 2:
        list_three.append(cards_21[i])

user_choose()

for i in range(2):
    cards_21 = []
    if user_column == 1:
        for i, card in enumerate(list_two):
            cards_21.append(list_two[i])

        for i, card in enumerate(list_one):
            cards_21.append(list_one[i])

        for i, card in enumerate(list_three):
            cards_21.append(list_three[i])

    elif user_column == 2:
        for i, card in enumerate(list_one):
            cards_21.append(list_one[i])

        for i, card in enumerate(list_two):
            cards_21.append(list_two[i])

        for i, card in enumerate(list_three):
            cards_21.append(list_three[i])

    elif user_column == 3:
        for i, card in enumerate(list_one):
            cards_21.append(list_one[i])

        for i, card in enumerate(list_three):
            cards_21.append(list_three[i])

        for i, card in enumerate(list_two):
            cards_21.append(list_two[i])

    list_one = []
    list_two = []
    list_three = []

    for i, card in enumerate(cards_21):
        if i%3 == 0:
            list_one.append(cards_21[i])
        elif i%3 == 1:
            list_two.append(cards_21[i])
        elif i%3 == 2:
            list_three.append(cards_21[i])

    user_choose()

def guess_card():
    cards_21 = list_two + list_one + list_three
    user_card = (cards_21[10])
    print("--------------------------------------")
    print("Your card is the {0}".format(user_card))
    print("--------------------------------------")

guess_card()
