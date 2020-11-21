#Stores current state of 3 x 3 board and has functions to populate, edit, update, and determines if win or loss conditions were met

import Deck
import PlayableStack
import DeadStack
import sys
import operator
import random

class Board:

    def __init__(self, deck):
        self.array = [[],[],[]]
        self.deck = deck

    #populates an empty matrix to represent the board
    #Used In: main, MonteCarlo.runMonteCarlo()
    def populate(self):
        #removes top 9 cards from Deck and creates 3x3 matrix of board
        self.deck.newDeck()
        counter = 0
        for row in self.array:
            if len(row) < 3:
                for i in range(3):
                    aliveStack = PlayableStack.PlayableStack([])
                    aliveStack.addCard(self.deck.draw())
                    self.array[counter].append(aliveStack)
            counter += 1

    #displays board to terminal
    #used in main, MonteCarlo.runMontedCarlo()
    def printBoard(self):
        for row in self.array:
            currentBoard = []
            for element in row:
                element.getTopCard
                currentBoard.append(element.getTopCard())
            print(currentBoard)

    #updates board by using a boolean, position, and a drawn card. Also prints board to terminal each time it's ran
    #Used In: main, MonteCarlo.runMonteCarlo()
    #Inputs: if the card drawn was higher or lower, the position of the original stack selected, card that was drawn
    def updateBoard(self, result, position, drawnCard):
        stack = self.array[position[0] - 1][position[1] - 1]
        if result == True:
            stack.addCard(drawnCard)
        if result == False:
            stack.addCard(drawnCard)
            deadStack = DeadStack.DeadStack()
            deadStack.copyPlayable(stack.getContents())
            self.array[position[0] - 1][position[1] - 1] = deadStack
        for row in self.array:
            printedBoard = []
            for element in row:
                if element.getStatus() == True:
                    printedBoard.append(element.getTopCard())
                if element.getStatus() == False:
                    printedBoard.append('X')
            print(printedBoard)

    #compares value of the stack that was initially guessed on vs the value of the card drawn
    #used in: main, MonteCarlo.runMonteCarlo()
    #Input: card drawn from deck, card at top of a stack, a guess
    #Returns: Boolean
    def compare(self, cardDrawn, topOfStack, guess):
        if guess == 3:
            guess = random.choice([1,2])
        if cardDrawn > topOfStack and guess == 1 or cardDrawn < topOfStack and guess == 0 or cardDrawn == topOfStack and guess == 2:
            return True
        else:
            return False
    
    #Checks if a win or loss condition has been met yet
    #used in: main, MonteCarlo.runMonteCarlo()
    #returns Boolean or None
    def checkWin(self):
        #uses isEmpty() in Deck class to determine if the deck is empty or not and then looks at itself
        #to see if there is any playable spots on the board still and returns string saying "Winner!"
        if self.deck.isEmpty() == True:
            for row in self.array:
                for element in row:
                    if element.getStatus() == True:
                        print()
                        print("Winner!")
                        print()
                        return True
                        
        counter = 0
        for row in self.array:
            for element in row:
                if element.getStatus() == False:
                    counter += 1
                if counter == 9:
                    print()
                    print("You Lost!")
                    print()
                    return True

    #gets which number is on the top of a stack based on stacks location
    #Used In: main, MonteCarlo.runMonteCarlo()
    #Input: [row number, column number]
    #Returns: a stacks top card
    def getChosen(self, position):
        #displays what number is on top of stack
        return (self.array[position[0] - 1][position[1] - 1]).getTopCard()

    #tells whether a stack is alive or dead based on stacks location
    #Used In: main, MonteCarlo.runMonteCarlo()
    #Input: [row number, column number]
    #Returns: a stacks alive or dead status
    def getStackStatus(self, position):
        return (self.array[position[0] - 1][position[1] - 1]).getStatus()

    #finds which card you have the best chance of getting correct in the matrix
    #Used In: main, MonteCarlo.runMonteCarlo()
    #returns: a card number
    def probStack(self): 
        card = 0
        highestDist = 0
        topCards = []
        for row in self.array:
            for stack in row:
                if stack.getStatus() == True:
                    topCards.append(stack.getTopCard())
        for i in topCards:
            currDist = abs(i - 8)
            if currDist > highestDist:
                card = i
                highestDist = currDist
        if highestDist == 0:
            card = 8
        return card

    #chooses a guess based on what cards are in the deck and what the value of the card chosen is
    #Used In: main
    #Input: card at top of a stack
    #Returns: a guess
    def choose(self, cardChosen):    
        higherCount = 0
        lowerCount = 0
        sameCount = 0
        for card in self.deck.getContents():
            if card > cardChosen:
                higherCount += 1
            if card < cardChosen:
                lowerCount += 1
            if card == cardChosen:
                sameCount += 1
        if lowerCount > higherCount:
            return 0
        if higherCount > lowerCount:
            return 1
        if sameCount == len(self.deck.getContents()):
            return 2
        if higherCount == lowerCount:
            return 3
        else: 
            return "Invalid choice"
        
    #Finds the location of a stack
    #Used In: main, MonteCarlo.runMonteCarlo()
    #Input: playable or dead stack
    #Returns: [Row Number, Column Number]
    def getLocation(self, bestStack):
        rowNum = 0
        colNum = 0
        for row in self.array:
            rowNum += 1
            colNum = 0
            for stack in row:
                colNum += 1
                if stack.getTopCard() == bestStack and stack.getStatus() != False:
                    return [rowNum, colNum]
        return "error: card not found"