import collections
from math import hypot

#예제1

class MyCollection :
    def __getitem__(self, key):
        return f"Value for {key}"
    
collection = MyCollection()
print(collection.__getitem__(3))
print(collection[3])

#예제2

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck :
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) :
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        
    def __len__(self) :
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

#예제3

beer_card = Card('7', 'diamonds')
beer_card

#예제4

deck = FrenchDeck()
print(f"Ranks: {deck.ranks}")
print(f"len: {len(deck)}")

#예제5

print(deck[0])
print(deck[-1])

#예제6

from random import choice

print(choice(deck))
print(choice(deck))
print(choice(deck))

#예제7

deck[:3]

#예제8

deck[12::13]

#예제9

for card in deck:
    print(card)

#예제10

for card in reversed(deck) :
    print(card)

#예제11

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value *len(suit_values) + suit_values[card.suit]

spades_high(beer_card)

for card in sorted(deck, key = spades_high) :
    print('The rank of {} is {}.'.format(card, spades_high(card)))

class Vector :
    def __init__(self, x = 0, y = 0) :
        self.x = x
        self.y = y
    
    def __repr__(self) :
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self) :
        return hypot(self.x, self.y)
    
    def __bool__(self) :
        return bool(abs(self))
    
    def __add__(self, other) :
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar) :
        return Vector(self.x * scalar, self.y * scalar)