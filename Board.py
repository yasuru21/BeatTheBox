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
        if guess == 3:
            guess = random.choice([1,2])
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

    #Mini-Max functions

    def parseStacks(self):
        lowerEight = 0
        higherEight = 0
        highLow = []
        for row in self.array:
            for stack in row:
                for cards in stack.getContents():
                    if cards < 8:
                        lowerEight += 1
                    if cards > 8:
                        higherEight += 1
        highLow.append(higherEight)
        highLow.append(lowerEight)
        return highLow
    
    def cardsPlayed(self):
        allCards = []
        for row in self.array:
            for stack in row:
                for cards in stack.getContents():
                    allCards.append(cards)
        return allCards
    
    def probDeck(self): #returns most likely cards to be picked from deck
        occurences = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}
        probs = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}
        highProbCards = []      #stores highest probable cards to pull from deck
        for card in Board.cardsPlayed(self):
            occurences[card] += 1
        for i in occurences:
            probs[i] = (4 - occurences[i]) / len(self.deck.getContents())
        highestProb = max(probs.values())
        for i in probs:
            if probs[i] == highestProb:
                highProbCards.append(i)
        return highProbCards

    def probStack(self): #returns which card you have the best chance of getting correct in the matrix
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

    def choose(self, cardChosen):   #returns 1 if guess should be higher, 0 if guess should be lower, and 3 if random guess is needed 
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

    def minimaxUpdate(self, tf, stack):
        loc = Board.getLocation(self, stack)
        if tf == False:
            deadStack = DeadStack.DeadStack()
            deadStack.copyPlayable(stack.getContents())
            stack = deadStack
            stack.addDead()
        self.array[loc[0]][loc[1]] = stack
        Board.printBoard(self)

    def aliveStacks(self):
        livingStacks = []
        for row in self.array:
            for stack in row:
                if stack.getStatus() != False:
                    livingStacks.append(stack)
        return livingStacks

    def getStack(self, topCard):
        loc = Board.getLocation(self, topCard)
        print(type(loc[0]))
        stack = self.array[loc[0] - 1][loc[1] - 1]
        if stack.getStatus == True:
            return stack

    def tempGuess(self, cardChosen, tempDeck):
        higherCount = 0
        lowerCount = 0
        sameCount = 0
        for card in tempDeck:
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
        if sameCount == len(tempDeck):
            return 2
        if higherCount == lowerCount:
            return 3
        else: 
            return "Invalid choice"