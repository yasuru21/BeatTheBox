import Board
import Deck
import random
import time 
import sys
import main

myDeck = Deck.Deck()
myBoard = Board.Board(myDeck)
cardsPlayed = []

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

    if len(myDeck.getContents()) <= 25:
        cardsLeft = myDeck.getContents()
        higher = 0
        lower = 0
        same = 0
        chances = []
        for val in cardsLeft:
            if val > probableStack:
                higher += 1
            if val < probableStack:
                lower += 1
            if val == probableStack:
                same += 1

        chances.append(lower/len(cardsLeft))
        chances.append(higher/len(cardsLeft))
        chances.append(same/len(cardsLeft))

        return chances.index(max(chances))


    sumProbs = 0
    for i in range(30000):
        sampSpace = possCards(myDeck)
        sumProbs += choice(sampSpace, probableStack)
    prob = sumProbs/30000
    print("prob: " + str(prob))
    if prob < 1:
        return 0
    if prob > 1:
        return 1

def runMonteCarlo():
    print("Initial Board")

    myBoard.populate()
    myBoard.printBoard()
    correctGuesses = 0
    wrongGuesses = 0

    for row in myBoard.array:
        for stack in row:
            cardsPlayed.append(stack.getTopCard())
    t1 = time.perf_counter()
    while True:
            if myBoard.checkWin():
                break

            print()

            location = myBoard.getLocation(myBoard.probStack())
            if myBoard.getStackStatus(location) != True:
                print("Invalid Stack")

            guess = monteCarlo(myBoard.probStack())
            chosen = myBoard.getChosen(location)
            cardDrew = myDeck.draw()
            cardsPlayed.append(cardDrew)

            print("Value Chosen: " + str(chosen))
            print("Card Drew: " + str(cardDrew))
            print("Guess: " + str(guess))
            print("deckLength: " + str(len(myDeck.getContents())))

            if myBoard.compare(cardDrew, chosen, guess):
                correctGuesses += 1
                print("Correct!")
                print()
                print("Updated Board")
                myBoard.updateBoard(True, location, cardDrew)
            else:
                wrongGuesses += 1
                print("Wrong")
                print()
                print("Updated Board")
                myBoard.updateBoard(False, location, cardDrew)
    t2 = time.perf_counter()
    print("Time: " + str(round(t2 - t1, 5)))
    print("Correct Guesses: " + str(correctGuesses))
    print("Incorrect Guesses: " + str(wrongGuesses))
    print("Cards Left in Deck: " + str(len(myDeck.getContents())))
    print()


    