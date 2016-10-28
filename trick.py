import random
card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
deck = []

def welcome_text():
    print("--------------------------------------")
    print("--------------------------------------")
    print("--------------------------------------")
    print("Welcome to the game. Please choose a card and I will try to guess it.")
    print("I will deal 21 cards in 3 columns. Pick a card in a column and tell me which one it is in")
    print("--------------------------------------")

def create_deck():
    for i in range (len(card_value)):
        deck.append(card_value[i]+ " of " + card_suit[0])
        deck.append(card_value[i]+ " of " + card_suit[1])
        deck.append(card_value[i]+ " of " + card_suit[2])
        deck.append(card_value[i]+ " of " + card_suit[3])

def deck_shuffle():
    random.shuffle(deck)

def take_21_cards():
    cards_21 = []
    for i in range(0,21):
        cards_21.append(deck[i])
        deck.pop(i)

def deal_cards():
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

def user_choose():
    print("--------------------------------------")
    print("Column one: {0}".format(list_one))
    print("--------------------------------------")
    print("Column two: {0}".format(list_two))
    print("--------------------------------------")
    print("Column three: {0}".format(list_three))
    print("--------------------------------------")
    user_column = input("Which column is your card in?: ")
    user_column = int(user_column)
    print("--------------------------------------")
    print("You have chosen column {0}".format(user_column))
    print("--------------------------------------")

def sort_columns():
    cards_21 = []
    if user_column == 1:
        for i, card in enumerate(list_two):
            cards_21.append(list_two[i])

    for i, card in enumerate(list_one):
        cards_21.append(list_one[i])

    for i, card in enumerate(list_three):
        cards_21.append(list_three[i])

    if user_column == 2:
        for i, card in enumerate(list_one):
            cards_21.append(list_one[i])

    for i, card in enumerate(list_two):
        cards_21.append(list_two[i])

    for i, card in enumerate(list_three):
        cards_21.append(list_three[i])

    if user_column == 3:
        for i, card in enumerate(list_one):
            cards_21.append(list_one[i])

    for i, card in enumerate(list_three):
        cards_21.append(list_three[i])

    for i, card in enumerate(list_two):
        cards_21.append(list_two[i])

def reveal_card():
    user_card = (cards_21[10])
    user_input = input("Do you want me to reveal your card?: ")
    if user_input== "yes":
        print("--------------------------------------")
        print("--------------------------------------")
        print("--------------------------------------")
        print("Your card is the {0}".format(cards_21[10]))
        print("Thanks for playing!")

def main():
    welcome_text()
    create_deck()
    deck_shuffle()
    take_21_cards()
    deal_cards()
    user_choose()
    sort_columns()
    reveal_card()

main()
