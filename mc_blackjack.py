import pydealer

class Card(object): 
    card_values = {
        'Ace': 11,
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

    def __init__(self, suit, value): 
        self.suit = suit.capitalize()
        self.value = value 
        self.point = self.card_values[value]

def ascii_card_image(card):
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']
    lines = [[] for i in range(9)]