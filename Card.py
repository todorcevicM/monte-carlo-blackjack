import pydealer
import numpy as np

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

def ascii_card_image(cards, add_inv = False):
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']
    lines = [[] for _ in range(9)]

    for index, card in enumerate(cards):
        if card.value == '10':
            value = card.value
            space = ''
        else:
            value = card.value[0]
            space = ' '

        suit = suits_symbols[suits_name.index(card.suit)]

        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(value, space))
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, value))
        lines[8].append('└─────────┘')
    
    result = []
    for index, _ in enumerate(lines):
        if (add_inv):
            lines[index].append(" ~ * * * ~ ")
            result.append(''.join(lines[index]))
        else:
            result.append(''.join(lines[index]))

    return '\n'.join(result)

def test(): 

    deck = pydealer.Deck()
    deck.shuffle()
    hand = deck.deal(2)
    dealer_visible = deck.deal(1)
    dealer_not_visible = deck.deal(1)

    pull = deck.deal(1)
    hand.add(pull)

    hand.cards[0]
    print("####### Dealer #######")
    print(ascii_card_image(dealer_visible.cards, True))
    print(">>----- Agents -----<<")
    print(ascii_card_image(hand.cards))
    print("######################")