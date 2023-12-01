# Tarot card game version 2
"""
Build a deck of cards
we will need the suits, ranks, tarot cards, and magic cards
"""

import random


def suits():
    ["Hearts", "Diamonds", "Spades", "Clubs"]


def ranks():
    {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1,
        "8": 1, "9": 1, "10": 1, "J": 2, "Kn": 3, "Q": 4, "K": 5}


def tarot():
    {"2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 1, "9": 1, "10": 1, "11": 1,
        "12": 1, "13": 1, "14": 1, "15": 1, "16": 1, "17": 1, "18": 1, "19": 1, "20": 1}


def special_cards():
    {"1": 5, "21": 5, "Excuse": 5}

    """Well shit the code below hasn't been working as expected, its late now so ill pick up on this later """
# def deck(suits, ranks, tarot, special_cards):
#     [(crd_type, suits) for suit in suits for crd_type in ranks] + [(crd_type, "Tarot") for crd_type in tarot] + [(crd_type "Special")] for crd_type in special_cards]


# if __name__ == "__main__":
#     players =
