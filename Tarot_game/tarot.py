# Tarot game


"""
<pre>
Nicolas Holmgren Chinique 
pdoc3 --html --force tarot.py
</pre>
"""

import random

# Creates the suits and the card rank
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

ranks = ['1', '2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'Jack', 'Knight', 'Queen', 'King']

"""Creates the tarot cards that are a total of 19 cards, 2-20, 1 is not included as it is a special card
this code loops through a range of 2, 21 to create the cards 2-20
"""
tarot = [str(i) for i in range(2, 21)]


# creates the magic cards, 1, 21, Excuse
magic_card = ['1', '21', 'Excuse']


"""This loops through the suits, ranks, tarot, and magic_cars to create the deck
crd_type will appear on the screen as the name it is assigned to so crd_type, Tarot, then tarot will be displayed along with the number

"""

deck = [(crd_type, suit) for suit in suits for crd_type in ranks] + [(crd_type, 'Tarot')
                                                                     for crd_type in tarot] + [(crd_type, 'Magic') for crd_type in magic_card]

# This randomly shuffles the deck
random.shuffle(deck)

# Asks for # of players, then divides cards Deal the cards to each player
num_players = int(input("How many players are you: "))

# This function selects a string from the deck list
middle_cards_3 = random.choice(deck)
print(middle_cards_3)

cards_per_player = len(deck) // num_players

hands = [deck[i:i+cards_per_player]
         for i in range(0, len(deck), cards_per_player)]

# this returns the player and there hand they have
for i in range(num_players):
    print(f"Player {i+1}'s hand: {hands[i]}")

# middle cards 3


"""
The code below is providing an incorrect result, that I have to fix, the while loop keeps going
"""
# while mission == "no":
for i in range(num_players):
    mission = str(input(f"Player {i+1} do you want to take the mission? "))
    if mission == "yes":
        mission_type = str(input("Do you take a SMALL, MEDIUM, or HIGH: "))
        if mission_type.lower() == "SMALL":
            print(f"Player {mission+1} takes a {mission_type}")

        while mission_type not in ["SMALL", "MEDIUM", "HIGH"]:
            mission_type = str(
                input("Do you take a SMALL, MEDIUM, or HIGH: "))
        print(f"Player {i+1} is taking the mission")
