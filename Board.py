#Stores current state of 3 x 3 board and has functions to populate, edit, update, and determines if win or loss conditions were met

class Board:
    int choice;
    def __init__(self, i):
        self.choice = i
        

    def populate(Deck):
        #removes top 9 cards from Deck and creates 3x3 matrix of board

    def updateBoard():
        #changes values on board after move is played and then prints board to console

    
    def compare(cardDrawn, stackPicked):
        #Sunil takes the drawn card and the player picked stack and compares the values of each and returns 
        topCard = stackPicked.getTopCard()
        if((cardDrawn > topCard) & (choice == 1)) | ((cardDrawn < topCard) & (choice == -1)) | ((cardDrawn == topCard) & (choice == 0)):
            stackPicked.addCard(cardDrawn)
        else:
            stackPicked.addCard(cardDrawn)
            self.convert(stackPicked)




    def winCondition():
        #uses isEmpty() in Deck class to determine if the deck is empty or not and then looks at itself
        #to see if there is any playable spots on the board still and returns string saying "Winner!"

    def lossCondition():
        #uses isEmpty() in Deck class to determine if the deck is empty or not and then looks at itself
        #to see if there is any playable spots on the board still and returns string saying "Loser!"
    
    def convert(playableStack):
        #Sunil converts a playable stack to a dead stack
        DeadStack a = new DeadStack(playableStack)
        
        #Then removes the stack in play on the board and replaces it with a new dead stack
         array.remove(playableStack)


        


    
