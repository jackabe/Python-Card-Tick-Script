import random

def welcome_text():
    print("Welcome to the game. Please pick a card. I will try to guess it.")
    print("I will deal 21 cards in 3 columns. Pick a card in a column and tell me which one it is in")
    print("--------------------------------------------------")

def create_shuffled_deck():
    # According to how many values present, each suit will be added to each value giving 52 cards.
    # Each card added to a list named 'deck'.
    # The deck is then shuffled.
    card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
    global deck # made global so deck can be used in future functions
    deck = []
    for i in range (len(card_value)):
        deck.append(card_value[i]+ " of " + card_suit[0])
        deck.append(card_value[i]+ " of " + card_suit[1])
        deck.append(card_value[i]+ " of " + card_suit[2])
        deck.append(card_value[i]+ " of " + card_suit[3])
        random.shuffle(deck)

def take_21_cards():
    # Pile of 21 cards is generated from the 52 cards.
    # Each card that is added from the 52 card deck is removed so it isn't duplicated.
    global cards_21 # made global so deck can be used in future functions.
    cards_21 = []
    for i in range(0,21):
        cards_21.append(deck[i])
        deck.pop(i)

def user_choose():
    # All three columns are printed to user_choose.
    # User is then asked to choose which column his card is in.
    print("Column one: {0}".format(column_one))
    print("--------------------------------------------------")
    print("Column two: {0}".format(column_two))
    print("--------------------------------------------------")
    print("Column three: {0}".format(column_three))
    print("--------------------------------------------------")
    global user_column
    user_column = input("Which column is your card in?: ")
    user_column = int(user_column)  # Cast to int so that it can be printed.
    print("You have chosen column {0}".format(user_column))
    print("--------------------------------------------------")

welcome_text()
create_shuffled_deck()
take_21_cards()

# Three columns are created.
# From the 21 card deck, a card is giuven to each column row by row.
# Enumerate is used because...
column_one = cards_21[0::3]
column_two = cards_21[1::3]
column_three = cards_21[2::3]

user_choose()

for i in range(2):
    # 21 card deck is emptied so that the cards can be re-added from the columns.
    # Whichever column the user chooses, it is sandwhiched between the other columns.
    # Columns are emptied so that the cards can be re-dealt from the re-structured 21 card deck.
    # Cards are re-dealt into the three columns, the user is asked to choose a column, and the process repeats 2 more times.
    cards_21 = []
    if user_column == 1:
        cards_21 = column_two + column_one + column_three
    elif user_column == 2:
        cards_21 =  column_one + column_two + column_three
    else:
        cards_21 = column_one + column_three + column_two

    column_one = cards_21[0::3]
    column_two = cards_21[1::3]
    column_three = cards_21[2::3]

    user_choose()

def guess_card():
    # 21 cards are then assembelled for the last time.
    # The 11th card is printed from the assembelled 21 deck.
    if user_column == 3:
        cards_21 = column_two + column_three + column_one
    elif user_column == 2:
        cards_21 =  column_one + column_two + column_three
    else:
        cards_21 = column_two + column_one + column_three
    user_card = (cards_21[10])
    print("--------------------------------------")
    print("Your card is the {0}".format(user_card))
    print("--------------------------------------")

guess_card()
