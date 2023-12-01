# from tarot import Tarot


# class Player:
#     def __init__(self, isDealer, deck):
#         self.cards = []
#         self.isDealer = isDealer
#         self.deck = deck
#         self.score = 0

#     # def hit(self):
#     self.cards.extend(self.deck)

# end = int(input("Enter a number: "))

# for i in range(end):
#     print(end)


class Card:
    def __init__(self, value, suit):
        self.cost = value
        self.value = ["2", "3", "4", "5", "6", "7",
                      "8", "9", "10", "J", "Kn", "Q", "K"]
        self.suit = ["Spade", "Diamond", "Club", "Heart"]

    def price(self):
        if self.cost <= 10:
            return 1
        if self.cost == "J":
            return 2
        if self.cost == "Kn":
            return 3
        if self.cost == "Q":
            return 4
        if self.cost == "K":
            return 5
        return self.cost
