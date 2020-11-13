import Board
import Deck
import sys
if __name__ == "__main__":
    myDeck = Deck.Deck()
    myBoard = Board.Board(myDeck)

    print()
    #print("Enter '1' for automated play (AI) or '2' for user play")
    #option = input()

    #if option == 1:
        #raise NotImplementedError

    #if option == 2:
    print("To guess higher, enter '1'. To guess lower, enter '0'")
    print()
    print("Initial Board")

    myBoard.populate()
    myBoard.printBoard()

    rowCol = []

    while True:
        myBoard.checkWin()

        while True:
            print()
            rowChoice = input("Choose Row: ")
            colChoice = input("Choose Column: ")
            rowCol.append(int(rowChoice))
            rowCol.append(int(colChoice))
            if myBoard.getStackStatus(rowCol) == True:
                break
            else:
                print("Invalid Stack: Try Again")
                rowCol.clear()
        
        guess = input("Enter Your Guess: ")
        cardDrew = myDeck.draw()

        print("\n""Value of Stack Chosen: " + str(myBoard.getChosen(rowCol)))
        print("Card Drew: " + str(cardDrew))

        if myBoard.compare(cardDrew, myBoard.getChosen(rowCol), int(guess)):
            print("Correct!")
            print()
            print("Updated Board")
            myBoard.updateBoard(True, rowCol, cardDrew)
        else:
            print("Wrong")
            print()
            print("Updated Board")
            myBoard.updateBoard(False, rowCol, cardDrew)

        rowCol.clear()
    

