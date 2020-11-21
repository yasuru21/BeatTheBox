#container to store cards in a playable stack
import Deck

class PlayableStack:

    def __init__(self, cards):
        self.contents = cards

    #Used In: Board.populate(), Board.updateBoard()
    #adds a card to itself
    #input: card from top of deck
    def addCard(self,cardPicked):
        #takes card from top of Deck and stores it
        self.contents.insert(0,cardPicked)

    #Used In: Board.getLocation(), Board.printBoard(), Board.updateBoard(), Board.probStack()#Used in: 
    #Returns: card from top of stack
    def getTopCard(self):
        return self.contents[0]

    #Used in: Board.updateBoard(), Board.checkWin, Board.getStackStatus(), Board.probStack()
    #Playable Stacks will always be True
    #Returns: True 
    def getStatus(self):
        return True
    
    #Used In: Board.updateBoard(), Board.choose()
    #Returns: contesnts of stack
    def getContents(self):
        return self.contents