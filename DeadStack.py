#container that stores cards in a dead stack

class DeadStack:
    
    def __init__(self):
        self.contents = []

    def copyPlayable(self, cards):
        for i in cards:
            self.contents.append(i)

    def getStatus(self):
        return False

    def getContents(self):
        return self.contents
    
    def getTopCard(self):
        return self.contents[0]

    def addDead(self):
        self.contents.insert(0, 'X')