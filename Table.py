
import Card


class Table(object):
    card_values = {
        'Ace_used': 1,
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

    def __init__(self):
        self.deck = Card.pydealer.Deck()
        self.deck.shuffle()
        self.hand = self.deck.deal(2)
        self.dealer_visible = self.deck.deal(1)
        self.dealer_not_visible = self.deck.deal(1)

        self.hand_sum = 0
        self.dealer_sum = 0
        for i in self.hand: 
            self.hand_sum += self.card_values[i.value]
        for i in self.dealer_visible:
            self.dealer_sum += self.card_values[i.value]
        
        if self.hand_sum > 21:
            for i in self.hand:
                if i.value == 'Ace':
                    i.value = 'Ace_used'
                    self.hand_sum -= 10
                    break
        

    def __str__(self):
        ret = "####### Dealer #######\n"
        ret += Card.ascii_card_image(self.dealer_v.cards, False) 
        ret += "\n>>----- Agents -----<<\n"
        ret += Card.ascii_card_image(self.hand.cards)
        ret += "\n######################\n"
        return ret

    def hit(self):
        new_card = self.deck.deal(1)
        self.hand_sum += self.card_values[new_card[0].value]
        self.hand.add(new_card)

        if self.hand_sum > 21:
            for i in self.hand:
                if i.value == 'Ace':
                    i.value = 'Ace_used'
                    self.hand_sum -= 10
                    return

    def check(self):
        self.dealer_visible.add(self.dealer_not_visible)
        self.dealer_sum += self.card_values[self.dealer_not_visible[0].value]

        while self.dealer_sum < 17:
            new_card = self.deck.deal(1)
            self.dealer_sum += self.card_values[new_card[0].value]
            self.dealer_visible.add(new_card)

        if self.dealer_sum > 21:
            for i in self.dealer_visible:
                if i.value == 'Ace':
                    i.value = 'Ace_used'
                    self.dealer_sum -= 10
                    break

 


