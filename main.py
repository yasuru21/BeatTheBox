import Board
import Deck
import sys
import MonteCarlo
import time


myDeck = Deck.Deck()
myBoard = Board.Board(myDeck)

#Explanation of benchmark algorithm and Monte Carlo are in README file

if __name__ == "__main__":

    print()
    print("Enter:")
    print("1 for user play")
    print("2 for one result of custom algorithm")
    print("3 for one result of Monte Carlo")
    option = input()
    print()

    myDeck = Deck.Deck()
    myBoard = Board.Board(myDeck)
    myBoard.populate()

    if option == "1":
        print("To guess higher, enter '1'. To guess lower, enter '0'. To guess the same, enter '2'")
        print()
        print("Initial Board")
        myBoard.printBoard()
        rowCol = []

        while True:
            if myBoard.checkWin():
                break

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

    if option == "2":
        print("Initial Board")

        myBoard.printBoard()
        correctGuesses = 0
        wrongGuesses = 0


        t1 = time.perf_counter()
        while True:
            rowCol = []

            if myBoard.checkWin():
                break

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

            if myBoard.compare(cardDrew, chosen, guess):
                correctGuesses += 1
                print("Correct!")
                print()
                print("Updated Board")
                myBoard.updateBoard(True, location, cardDrew)
            else:
                wrongGuesses += 1
                print("Wrong")
                print()
                print("Updated Board")
                myBoard.updateBoard(False, location, cardDrew)
        t2 = time.perf_counter()
        print("Time: " + str(round(t2 - t1, 5)))
        print("Correct Guesses: " + str(correctGuesses))
        print("Incorrect Guesses: " + str(wrongGuesses))
        print("Cards Left in Deck: " + str(len(myDeck.getContents())))
        print()


    if option == "3":
        MonteCarlo.runMonteCarlo()