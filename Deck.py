#container that stores all cards

import random

class Deck:

    def __init__(self):
        self.contents = []

    def newDeck(self):
        #populates the deck randomly
        suit = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in range(4):
            for j in suit:
                self.contents.append(j)
        random.shuffle(self.contents)

    def isEmpty(self):
        #checks if deck still has members and returns true if empty and false if not empty
        if len(self.contents) != 0:
            return False
        else:
            return True
    
    def draw(self):
        #returns top card from the deck
        #print("length of deck: " + str(len(self.contents)))
        if len(self.contents) > -1: 
            return self.contents.pop(0)
        else:
            print("Error: No cards in deck")

    def getContents(self):
        return self.contents