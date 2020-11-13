#Stores current state of 3 x 3 board and has functions to populate, edit, update, and determines if win or loss conditions were met

import Deck
import PlayableStack
import DeadStack
import sys

class Board:

    def __init__(self, deck):
        self.array = [[],[],[]]
        self.deck = deck

    def populate(self):
        #removes top 9 cards from Deck and creates 3x3 matrix of board
        self.deck.newDeck()
        counter = 0
        for row in self.array:
            if len(row) < 3:
                for i in range(3):
                    aliveStack = PlayableStack.PlayableStack()
                    aliveStack.addCard(self.deck.draw())
                    self.array[counter].append(aliveStack)
            counter += 1

    def printBoard(self):
        for row in self.array:
            currentBoard = []
            for element in row:
                element.getTopCard
                currentBoard.append(element.getTopCard())
            print(currentBoard)

    def updateBoard(self, result, position, drawnCard):
        #changes values on board after move is played and then prints board to console
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


    def compare(self, cardDrawn, topOfStack, guess):
        #takes the drawn card and the player picked stack and compares the values of each and returns if whether they 'won' or 'lost'
        if cardDrawn > topOfStack and guess == 1 or cardDrawn < topOfStack and guess == 0 or cardDrawn == topOfStack and guess == 2:
            return True
        else:
            return False
        

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
                        sys.exit()
                        
        counter = 0
        for row in self.array:
            for element in row:
                if element.getStatus() == False:
                    counter += 1
                if counter == 9:
                    print()
                    print("You Lost!")
                    print()
                    sys.exit()


    def getChosen(self, position):
        #displays what number is on top of stack
        return (self.array[position[0] - 1][position[1] - 1]).getTopCard()

    def getStackStatus(self, position):
        return (self.array[position[0] - 1][position[1] - 1]).getStatus()



    
