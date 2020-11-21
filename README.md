# BeatTheBox
CSCI-B 351 final project

Objective:

Beat the Box is a card game played by randomizing a normal deck of cards and placing them faceup in a 3x3 square. The idea of the game is the player will pick one of the cards in the square and guess one of three options which are higher, lower, or the same (push) as the number on the card on top of the chosen stack. After the guess, you will take a card from the top of the deck and place it on the stack which was picked. If a player guesses wrong, then they can’t play on that stack any more. You must do this over and over until there are no cards left in the deck or all stacks are flipped over, resulting in a loss.

Rules:

- Cards must be in a 3x3 square
- Cards to create initial 3x3 must be chosen from top of shuffled deck
- Cards must be re-shuffled after each game
- Must choose stack prior to taking card off top of deck
- If you guess “higher” the card off the top of the deck must be higher than the card on top of the players chosen stack and vice versa  for “lower”
- If you guess “push” the card off the top of the deck must be the same as the card on top of your chosen stack
- When someone is right place card from top of deck on chosen stack and continue playing
- When someone is wrong, leave the card placed on top of the stack and flip over the entire stack marking it as a dead stack
- Once a stack is dead you can’t play on it anymore 
- If all stacks in the 3x3 are dead and you still have cards in the deck you lose the game
- If all cards in the deck are gone and not all stacks are dead then you win the game
- Use standard 52 card deck
- Suit doesn’t matter

In order to play the game simply run "main.py" file in your terminal and follow the directions

Main algorithms implementation:

Custom Algorithm:
	•	Uses 2 functions to compute a guess
	◦	Board.probStack()
	    ▪	Checks each stack in the array and compiles a list (topCards) of which card is on the top of each stack
	    ▪	Loops over topCards and compares the absolute value of |card value - 8| since 8 is the hardest card to guess correctly on
	    ▪	Uses the largest absolute value to determine which card it should pick from the board
	    ▪	Returns which card on the board should be played

	◦	Board.choose(mostProbableStack)
	    ▪	Input is which card on the board should be played (Board.probStack)
	    ▪	Finds which cards are still left in the deck and then compares if they are higher, lower or the same value as the best       option card in the board
	    ▪	Depending on if there are more higher, lower or the same cards, it returns a guess of 0(lower), 1(higher), or 2(same)

	▪	Monte Carlo Algorithm:
	    ▪	Uses three functions to compute a guess
	        ▪	MonteCarlo.possCards(currDeck)
	            ▪	Creates and returns a sample space of what cards are still left in the deck
	            ▪	MonteCarlo.choice(possCards, bestInBoard)
	            ▪	Input is sample space (current deck) and most probable card to pick correctly on in board (Board.probStack())
	            ▪	Finds a count of what cards in the sample space are higher, lower or the same as the best possible choice stack from the board
	            ▪	Depending on which amount of cards are lower, higher, or the same, it returns a number which is either 
	                (amount of cards lower than chosen card / length of current deck) 
	                or
	                (length of current deck / amount of cards lower than chosen card) 
	        ▪	MonteCarlo.monteCarlo()
	            ▪	Input is most probable card to pick correctly on in board (Board.probStack())
	            ▪	Runs 30000 iterations of possCards() and choice() in order to find the sum of all the calculated values
	            ▪	Divides the sum found by how many iterations it went through to obtain a value 
                ▪	Checks whether this value is >,< or within a specific range of 1 
	            ▪	Note: the value of 1 was determined through testing not any actual coding
	            ▪	This algorithm was consistently failing to pick the correct cards in order if the deck was smaller than a certain   number so I implemented the following mini algorithm to make better choices
	                ▪	If the deck is below a certain length, find the probabilities of pulling a higher card, lower card, or same card and whichever probability is highest, return that guess.
