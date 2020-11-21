#container that stores all cards

import random

class Deck:

    def __init__(self):
        self.contents = []

    #Generates a random deck of cards 2-14 four times to represent each suit 
    #Used In: Board.populate()
    def newDeck(self):
        suit = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in range(4):
            for j in suit:
                self.contents.append(j)
        random.shuffle(self.contents)

    #Checks to see if the deck is empty
    #Used In: Board.checkWin()
    #Returns: Boolean
    def isEmpty(self):
        if len(self.contents) != 0:
            return False
        else:
            return True

    #takes top card out of deck
    #Used In: Board.populate(), MonteCarlo.runMonteCarlo()
    #Returns: Card at top of deck
    def draw(self):
        if len(self.contents) > -1: 
            return self.contents.pop(0)
        else:
            print("Error: No cards in deck")

    #gives a list of all contents within the deck
    #Used in: Board.updateBoard(), Board.choose(), MonteCarlo.possCards(), MonteCarlo.monteCarlo()
    #Returns: list of cards
    def getContents(self):
        return self.contents