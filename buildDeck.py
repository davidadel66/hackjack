import random

class Cards:
    def __init__(self, numDecks=1):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'King', 'Queen', 'Jack']
        self.suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        self.deck = []
        for i in range(numDecks):
            deck = self._make_deck()
            self.deck.extend(deck)

    def _show_deck(self):
        print(f'Length of deck', len(self.deck))
        print(self.deck)
        print()

    def _make_deck(self):
        return [(suit, rank) for suit in self.suits for rank in self.ranks]

    def _shuffle(self):
        return random.shuffle(self.deck)
    
    def _deal(self, n=1):
        dealt, self.deck = self.deck[:n], self.deck[n:]
        return dealt

if __name__ == "__main__":
    pass


    


    



