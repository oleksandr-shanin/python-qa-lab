from random import shuffle
from copy import deepcopy


class Card:
    suits = {'spades': '♠', 'clubs': '♣', 'diamonds': '♦', 'hearts': '♥'}
    denominations = ['R*', 'B*', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'J', 'Q', 'K', 'A']
    names = ['Red Joker', 'Black Joker', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, denomination, suit=None):
        if suit and suit not in self.suits:
            raise ValueError('{} is not one of allowed: {}'.format(suit, self.suits))
        if not (0 <= denomination <= 14 and type(denomination) is int):
            raise ValueError('Denomination has to be int from 0 to 14')
        if denomination in {0, 1} and suit:
            raise ValueError('The Joker has no suit')
        self.suit = suit
        self.denomination = denomination

    def __repr__(self):
        if self.denomination in {0, 1}:
            return 'Card({})'.format(self.denomination)
        else:
            return "Card({}, '{}')".format(self.denomination, self.suit)

    def __str__(self):
        if self.suit:
            return self.denominations[self.denomination] + self.suits[self.suit]
        else:
            return self.denominations[self.denomination]

    def long_name(self):
        result = self.names[self.denomination]
        if self.denomination >= 2:
            result += ' of {}'.format(self.suit)
        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Deck:
    def __init__(self, full_deck):
        self.cards = []
        self.full_deck = full_deck
        if full_deck == 24:
            for suit in Card.suits:
                for denomination in range(9, 15):
                    self.cards.append(Card(denomination, suit))
        elif full_deck == 32:
            for suit in Card.suits:
                for denomination in range(7, 15):
                    self.cards.append(Card(denomination, suit))
        elif full_deck == 36:
            for suit in Card.suits:
                for denomination in range(6, 15):
                    self.cards.append(Card(denomination, suit))
        elif full_deck == 52:
            for suit in Card.suits:
                for denomination in range(2, 15):
                    self.cards.append(Card(denomination, suit))
        elif full_deck == 54:
            for suit in Card.suits:
                for denomination in range(2, 15):
                    self.cards.append(Card(denomination, suit))
            self.cards.append(Card(0))
            self.cards.append(Card(1))
        else:
            raise ValueError('Number of cards in the deck is not one of the allowed: 24, 32, 36, 52, 54'.format(full_deck))

    def __repr__(self):
        return 'Deck({})'.format(self.full_deck)

    def __str__(self):
        result = ''
        i = 0
        for card in self.cards:
            result += str(card).rjust(4)
            i += 1
            if not i % (self.full_deck // 4):
                result += '\n'
        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        try:
            return self.cards.pop(0)
        except IndexError:
            raise IndexError('Draw from empty deck')

    def add(self, card):
        if not isinstance(card, Card):
            raise TypeError('You can only add card to a deck')
        if card in self.cards:
            raise ValueError('In the Deck there can be only one {}'.format(card))
        if card.denomination < 9 and self.full_deck == 24 or\
           card.denomination < 6 and self.full_deck == 36 or\
           card.denomination < 7 and self.full_deck == 32 or\
           card.denomination < 2 and self.full_deck == 52:
            raise ValueError('{} is not allowed in {}-card deck'.format(card, self.full_deck))
        self.cards.append(card)


if __name__ == '__main__':
    deck1 = Deck(24)
    deck2 = Deck(24)
    assert deck1 == deck2, 'Deck equality test fail'
    deck2.shuffle()
    assert deck1 != deck2, 'Shuffle test fail'
    deck1 = deepcopy(deck2)
    for i in range(deck2.full_deck):
        deck2.add(deck2.draw())
    assert deck1 == deck2, 'Draw/add test fail'
