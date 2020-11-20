import Board
import Deck
import sys
import MiniMax

if __name__ == "__main__":
    myDeck = Deck.Deck()
    myBoard = Board.Board(myDeck)

    print()
    print("Enter '1' for Mini-Max play, '2' for user play and '3' for group built AI")
    #option = input()
    print()

    #if option == "1":

    MiniMax.runMiniMax()

    if option == "3":
        print("Initial Board")

        myBoard.populate()
        myBoard.printBoard()

        while True:
            rowCol = []

            myBoard.checkWin()

            print()

            location = myBoard.getLocation(myBoard.probStack())
            if myBoard.getStackStatus(location) != True:
                print("Invalid Stack")

            guess = myBoard.choose(myBoard.probStack())
            cardDrew = myDeck.draw()
            chosen = myBoard.getChosen(location)

            print("Value Chosen: " + str(chosen))
            print("Card Drew: " + str(cardDrew))
            print("Guess: " + str(guess))
            print("deckLength: " + str(len(myDeck.getContents())))

            if myBoard.compare(cardDrew, chosen, guess):
                print("Correct!")
                print()
                print("Updated Board")
                myBoard.updateBoard(True, location, cardDrew)
            else:
                print("Wrong")
                print()
                print("Updated Board")
                myBoard.updateBoard(False, location, cardDrew)

        

    if option == "2":
        print("To guess higher, enter '1'. To guess lower, enter '0'. To guess the same, enter '2'")
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
                print()
                print("Correct!")
                print("Updated Board")
                myBoard.updateBoard(True, rowCol, cardDrew)
            else:
                print("Wrong")
                print()
                print("Updated Board")
                myBoard.updateBoard(False, rowCol, cardDrew)
            rowCol.clear()