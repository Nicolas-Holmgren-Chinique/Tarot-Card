import random
# declaring the cards in the card game


class Card:
    def __init__(self, value, suit, tarot, magic_cards):
        self.points = value
        self.value = value
        self.suit = suit
        self.tarot = tarot
        self.magic_cards = magic_cards


def __str__(self):
    return f"{self.value} {self.special_ability}"


def create_cards():
    deck = []
    for _ in range(15):
        for suit in ["Spade", "Diamond", "Heart", "Club"]:
            for value in ["1", "2", "3", "4", "5", "6",
                          "7", "8", "9", "10", "Jack", "Knight", "Queen", "King"]:
                for tarot in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                              "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
                    for magic_cards in ["1", "21", "Joker"]:
                        deck.append(Card(value, suit, tarot, magic_cards))


# random.shuffle(Card)
num_player = int(input("How many players' are you: "))
hand_size = 15
hands = [[] for i in range(num_player)]
for i in range(hand_size):
    for j in range(num_player):
        hands[j].append(Card.pop())

for i in range(num_player):
    print([hands(i)])

# the variable asks the uer for input on how many people are playing the game
number_players = int(input("Enter amount of players: "))

# the money amount counter is set to 0
money_amount = 0


# The for loop gets the number of players and asks each one to input the amount of money they wish to bet and each time a user puts in money it goes into the pot which adds up all the money the users input
for i in range(number_players):
    money_amount += int(input("Enter amount of money you want to bet: "))
    print("There is: $", money_amount, "on the table")

# this is for the processing fee and what the winners will get after the fee
fee = money_amount * .10
new_money_amount = money_amount - fee

# random number between 0, 20 this will make a random number
random_num = random.randint(0, 20)


while True:
    winner = False
    for i in range(number_players):
        guess = int(
            input("Player {} guess a number between 0-20: ".format(i+1)))
        if guess == random_num:
            print("Player", i+1, "won with a correct guess of", guess,
                  "Player gets the money pool, player wins: $", new_money_amount)

            winner = True
            break
    if winner:
        break
    print("No one won, lets do it again")


# define the tarot cards
cards = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
         "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
         "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
         "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgment", "The World"]

# shuffle the deck
# random.shuffle(Card)

# deal cards to players
add_players = int(input("How many players' are you: "))
num_players = add_players
hand_size = 3
hands = [[] for i in range(num_players)]
for i in range(hand_size):
    for j in range(num_players):
        hands[j].append(Card.pop())

# print the hands of each player
for i in range(num_players):
    print('Player', i + 1, ':', hands[i])


start_game = str(input("Press 'S' to start the game"))

if start_game == "s":
    print("starting game")

rules = print("You each have 15 cards, 3 cards are in the middle, those cards are for whomever takes the mission \n there are 3 magic cards that are all worth a lot of point \n the 1 the 21 and the excuse..... ")

small = 1
medium = 2
high = 3

player1 = str(
    input("Do you want to take the mission, if so which one small, medium or high: "))


# players = player2, player3, player4, player5

if player1 != "small" or "medium" or "high":
    print("you may only take the mission if all other players don't take a higher mission then you")


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'Jack', 'Knight', 'Queen', 'King']

tarot = [str(i) for i in range(2, 21)]

magic_card = ['1', '21', 'Excuse']
deck = [(rank, suit) for suit in suits for rank in ranks] + [(rank, 'Tarot')
                                                             for rank in tarot] + [(rank, 'Magic') for rank in magic_card]

# Shuffle the deck
random.shuffle(deck)

# Deal the cards to each player
num_players = input("How many players are you: ")
while not num_players.isdigit() or int(num_players) <= 0:
    num_players = input(
        "Please enter a positive integer for the number of players: ")
num_players = int(num_players)

cards_per_player = len(deck) // num_players
hands = {
    f"Player {i+1}": deck[i*cards_per_player:(i+1)*cards_per_player] for i in range(num_players)}

for player, hand in hands.items():
    print(f"{player}'s hand: {hand}")


# Ask each player if they want to take the mission
missions = {}
for i in range(num_players):
    mission = input(
        f"Player {i+1}, do you want to take the mission? (yes or no) ")
    while mission.lower() not in ["yes", "no"]:
        mission = input("Please enter 'yes' or 'no': ")

    if mission.lower() == "yes":
        mission_type = input("Do you take a SMALL, MEDIUM, or HIGH mission? ")
        while mission_type.lower() not in ["small", "medium", "high"]:
            mission_type = input("Please enter 'SMALL', 'MEDIUM', or 'HIGH': ")
        print(f"Player {i+1} is taking the {mission_type.upper()} mission")

        missions[f"Player {i+1}"] = mission_type.upper()
