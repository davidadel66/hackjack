from buildDeck import Deck
from random import shuffle 

class BlackJack:
    def __init__(self, numShoes=1):
        self.Deck = Deck(numDecks=numShoes)
        self.fullCardCount = numShoes * 52
        self.playerScore = 0
        self.playerSoftScore = 0
        self.dealerScore = 0
        self.resetGame = False
        self.playerBust = False
        self.dealerBust = False
        self.playerWin = False
        self.dealerWin = False
        
    @property
    def cutCard(self):
        return len(self.Deck.cards) <= (self.fullCardCount // 2)
    
    def _addNum(self, card, soft=False):
        if card[1] == "Ace":
            return 1 if soft else 11
        if card[1].isin(["King", "Queen", "Jack"]):
            return 10
        else: 
            return card[1]

    
    def _deal(self):
        """
        Need to simulate the deal function of blackjack; 
        first card dealt to player -> second card to dealer face up
        third card to player -> fourth card to dealer face down
        """
        for i in range(1, 5):
            card = self.Deck.cards.pop(0)
            if card[1] == "Ace":
                self.playerScore += 11
                self.playerSoftScore += 1
            elif card[1].isin(["King", "Jack", "Queen"]):
                self.playerScore += 10
                self.playerSoftScore += 10
            else:
                self.playerScore += card[1]
                self.playerSoftScore += card[1]
    
        pass

    def testCutCard(self):
        while not self.cutCard:
            self.Deck._shuffle()
            cards = self.Deck.cards
            print(cards)
            cards.pop(0)
            print()
            print(cards)
            print(cards[0][1])
        print('Cut Card appeared')
        
        
        

        
if __name__ == "__main__":
    jack = BlackJack()
    jack.testCutCard()


