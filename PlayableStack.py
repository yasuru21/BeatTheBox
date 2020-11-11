#container to store cards in a playable stack
import Deck

class PlayableStack:

    def __init__(self):
        self.contents = []


    def addCard(self,cardPicked):
        #takes card from top of Deck and stores it
        self.contents.insert(0,cardPicked)

    def getTopCard(self):
        return self.contents[0]

    def getStatus(self):
        return True
    
    def getContents(self):
        return self.contents