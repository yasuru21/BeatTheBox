#container that stores cards in a dead stack

class DeadStack:
    
    def __init__(self):
        self.contents = []

    #fills itself with a copy of a playable stack
    #Used in: Borad.updateBoard()
    #Input: PlayableStack.PlayableStack()
    def copyPlayable(self, cards): 
        for i in cards:
            self.contents.append(i)

    #All deadStack status' are False
    #Used in: Board.updateBoard(), Board.checkWin, Board.getStackStatus(), Board.probStack()
    #Board.getLocation(), Board.aliveStacks(), Board.getStack
    #Returns: False
    def getStatus(self):
        return False

    #Used In: Board.updateBoard(), Board.choose()
    #returns a list of values in the stack
    def getContents(self):
        return self.contents
    
    #Used In: Board.getLocation(), Board.printBoard(), Board.updateBoard(), Board.probStack()
    #returns whatever card is at top of the stack
    def getTopCard(self):
        return self.contents[0]