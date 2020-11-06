# BeatTheBox
CSCI-B 351 final project

Objective:

Beat the Box is a card game played by randomizing a normal deck of cards and placing them faceup in a 3x3 square. The idea of the game is the player will pick one of the cards in the square and guess one of three options which are higher, lower, or the same (push) as the number on the card on top of the chosen stack. After the guess, you will take a card from the top of the deck and place it on the stack which was picked. If a player guesses wrong, then they can’t play on that stack any more. You must do this over and over until there are no cards left in the deck or all stacks are flipped over, resulting in a loss.

Rules:

- Cards must be in a 3x3 square
- Cards to create initial 3x3 must be chosen from top of shuffled deck
- Cards must be re-shuffled after each game
- Must choose stack prior to taking card off top of deck
- If you guess “higher” the card off the top of the deck must be higher than the card on top of the players chosen stack and vice versa    for “lower”
- If you guess “push” the card off the top of the deck must be the same as the card on top of your chosen stack
- When someone is right place card from top of deck on chosen stack and continue playing
- When someone is wrong, leave the card placed on top of the stack and flip over the entire stack marking it as a dead stack
- Once a stack is dead you can’t play on it anymore 
- If all stacks in the 3x3 are dead and you still have cards in the deck you lose the game
- If all cards in the deck are gone and not all stacks are dead then you win the game
- Use regular deck of cards with no joker
- Suit doesn’t matter
- Order of High cards: 10, Jack, Queen, King, Ace
