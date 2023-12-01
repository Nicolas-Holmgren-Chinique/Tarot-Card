# define the point values for each card
card_points = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

# example list of cards
cards = ['Ace', '5', 'King', 'Queen']

# calculate the total points for the cards
total_points = 0
for card in cards:
    total_points += card_points[card]

print('Total points:', total_points)
