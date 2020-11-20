import Board
import Deck
import random
import time 
import numpy

myDeck = Deck.Deck()
myBoard = Board.Board(myDeck)
myBoard.populate()

def possCards(currDeck):
    sampleSpace = []
    if len(currDeck.getContents()) >= 0:
        for card in currDeck.getContents():
            sampleSpace.append(card)
    return sampleSpace


def choice(possCards, bestInBoard):
    lenPoss = len(possCards)
    higherCount = 0
    lowerCount = 0
    sameCount = 0
    for card in possCards:
        if card > bestInBoard:
            higherCount += 1
        if card < bestInBoard:
            lowerCount += 1
        if card == bestInBoard:
            sameCount += 1
    if lowerCount > higherCount:
            return lowerCount/lenPoss
    if higherCount > lowerCount:
        return lenPoss/higherCount
    if sameCount == lenPoss:
        return 0
    if higherCount == lowerCount:
        return random.choice([lowerCount/lenPoss, lenPoss/higherCount])
    else: 
        return "Invalid choice"

def monteCarlo(probableStack):
    highRange = len(myDeck.getContents())

    sumProbs = 0
    for i in range(500):
        sampSpace = possCards(myDeck)
        sumProbs += choice(sampSpace, probableStack)
    
    return sumProbs/500

bestCard = 4
nextCard = 10

print()
print("card chosen: " + str(bestCard))
print("next card: " + str(nextCard))
print(monteCarlo(myBoard.probStack()))
print()

    