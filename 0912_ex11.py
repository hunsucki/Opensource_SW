#예제11

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value *len(suit_values) + suit_values[card.suit]

spades_high(Beer_card)

for card in sorted(Deck, key = spades_high) :
    print('The rank of {} is {}.'.format(card, spades_high(card)))

