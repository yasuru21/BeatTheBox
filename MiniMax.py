#implements mini-max search algorithm

import random
import time 
import Board
import Deck
import sys          #DEBUG setting recursion limit
sys.setrecursionlimit(10**6)

myDeck = Deck.Deck()
myBoard = Board.Board(myDeck)
myBoard.populate()

class Node(object):

    def __init__(self, depth, stackVal):
        self.depth = depth
        self.stackVal = stackVal
        self.children = []
        self.tempDeck = myDeck.getContents()
        self.createChildren()
        

    def createChildren(self):
        print("DEPTH: " + str(self.depth))
        print("stack value: " + str(self.stackVal))
        
        if self.depth > 0 and Node.checkParent(self):     #DEBUG testing or instead of and
            for i in range(len(self.tempDeck)):
                print("i: " + str(i))
                self.children.append(Node(self.depth - 1, self.tempDeck.pop(0)))

    def checkParent(self):
        return myBoard.compare(self.stackVal, self.tempDeck[0], myBoard.tempGuess(self.stackVal, self.tempDeck))
    
    def checkChildren(self):
        if self.children:
            return True
        if self.children == []:
            return False
        else:
            print("CheckChildren: Children not found")

def minimax(node, depth):
    myCards = []
    print("inside Minimax")
    if depth == 0 or len(myDeck.contents()) <= 0 or node.stackVal == 'X':
        print("inside first if")
        return PlayableStack.PlayableStack()
    
    goalVal = 0
    maxSize = 52
    allDepths = []

    print("len childNodes: " + str(len(node.children)))
    allVals = []
    for i in node.children:
        if myBoard.compare(myDeck.draw()):
            childMax = minimax(node, node.depth - 1)
            if childMax.checkChildren() == False or guess == 'X':
                allDepths.append(childMax.depth())
                maxDepth = max(allDepths)
            
    

    return goalVal


def runMiniMax():
    for stack in myBoard.aliveStacks():
        node = Node(len(myDeck.getContents()), myBoard.probStack())
        minimax(node, len(myDeck.getContents()))

    


    

