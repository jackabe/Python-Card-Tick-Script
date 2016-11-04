import random
import os
import time
import textwrap

def cls():
    # Clears the function from the client after x amount of seconds - found on Stack Overflow.
    os.system('cls' if os.name=='nt' else 'clear')

def welcome_text():
    # Prints out the introduction but wraps (after 70 characters) so the lines have a consistent indent.
    # The next function dosn't carry out for 3 seconds.
    welcome_str = "Welcome to the game. I will deal 21 cards in 3 columns. Pick a card in a column and tell me which one it is in. I will re-deal the cards 2 further times and ask you again which column your card is in."
    print(textwrap.fill(welcome_str, 70))
    print("--------------------------------------------------")
    time.sleep(3)

def create_shuffled_deck():
    card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    card_suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
    deck = []
    for i in range (len(card_value)):
        deck.append(card_value[i]+ " of " + card_suit[0])
        deck.append(card_value[i]+ " of " + card_suit[1])
        deck.append(card_value[i]+ " of " + card_suit[2])
        deck.append(card_value[i]+ " of " + card_suit[3])
        random.shuffle(deck)
    return deck

def take_21_cards():
    # Pile of 21 cards is generated from the 52 cards.
    # Each card that is added from the 52 card deck is removed so it isn't duplicated.
    global cards_21 # made global so deck can be used in future functions.
    cards_21 = []
    for i in range(0,21):
        cards_21.append(deck[i])
        deck.pop(i)

def user_choose():
    # All three columns are printed to the user.
    # User is then asked to choose which column their card is in.
    # While loop to check the input is a digit and either 1,2, or 3.
    # Clears once the user has chosen a column.
    print("Column one: {0}".format(column_one))
    print("--------------------------------------------------")
    print("Column two: {0}".format(column_two))
    print("--------------------------------------------------")
    print("Column three: {0}".format(column_three))
    print("--------------------------------------------------")
    global user_column
    while True:
        user_column = input("Which column number is your card in: 1, 2 or 3?: ")  # Cast to an int so I can print it within a string.
        user_column = int(user_column)
        if 1 <= user_column <=3:
            print("You have chosen column {0}".format(user_column))
            print("--------------------------------------------------")
            break
        else:
            continue
            print("Not a valid number")
    cls()

welcome_text()
deck = create_shuffled_deck()
take_21_cards()

# Three columns are created.
# From the 21 card deck, a card is giuven to each column row by row.
# I have used slices here as it is very easy way to deal out the cards without for loops which I did originally. Found on Stack Overflow.
column_one = cards_21[0::3] # The 0 is telling it to deal the first card in list to the first column and then deal every third card after this point.
column_two = cards_21[1::3] # The 1 is telling it to deal the second card in list to the second column and then deal every third card after this point.
column_three = cards_21[2::3] # The 2 is telling it to deal the third card in list to the thrid column and then deal every third card after this point.

user_choose()

for i in range(2):
    # 21 card deck is emptied so that the cards can be re-added from the columns.
    # Whichever column the user chooses, it is sandwhiched between the other columns.
    # Cards are re-dealt into the three columns, the user is asked to choose a column, and the process repeats 2 more times.
    # Function clears once user has chosen column.
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
    cls()

def guess_card():
    # 21 cards are then assembelled for the last time with the chosen column sandwhiched.
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
    print("Thank you for playing the game, By Jack Allcock C1673107")

guess_card()
