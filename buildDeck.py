import random

class Deck:
    def __init__(self, numDecks=1):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'King', 'Queen', 'Jack']
        self.suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        self.numDecks = numDecks
        self.cards = self._make_deck()

    def _make_deck(self):
        return [(suit, rank) for suit in self.suits for rank in self.ranks] * self.numDecks

    def _shuffle(self):
        return random.shuffle(self.cards)
    

if __name__ == "__main__":
    pass


    


    



