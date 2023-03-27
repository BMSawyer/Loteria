# Loteria
The game file is game_user_prompt.py
Alternate game file (no user inputs required) is game.py

My game is a single player game which arranges a board of 16 randomly selected personas, and shuffles the deck of 54 cards.
The board simply displays the titles of the cards in a grid by using print statements.

I created 2 classes of objects for the game.  

1- The DrawDeck class, which takes a list as a parameter and retains a working copy of a list of lists (representing the cards). Each 'card' in the list is itself a list containing the id, the name, and the verse as elements.  
The order of the cards are randomized when the object is created.

DrawDeck has a .draw method, which returns the card in the 0th position, using a .pop method, so the deck gets smaller as each card is drawn.

2- The Board class is where most of the action happens.  The Board class takes a list (a deck of cards) as a paramter, randomizes the list and loops through the first 16 cards, writing them into a cards_on_board list.  

The .layout method then prints the board as a 4 x 4 grid.

The .mark method takes a parameter of a list (card) and loops through the cards on board to see if there is a match.  if yes, the card title is updated as BEAN and the id value =1000.  Then the .layout is called again to reset the board. 

The .calc method takes no arguments and simply includes if and elif evaluations to determine whether there are 4 beans on the board in a row or column, by summing the ids.  If the sum of a row or column is 4 * 1000, then it is a winner and a boolean variable called won is set to True.

Game play starts with the user pressing any key, and runs in a loop while won = False.  The user is asked to type a key to draw a new card on each turn.  The card title and verse are displayed, and the board is redrawn on each turn, with any matching cards showing BEAN.  

Eventually, a winning scenario is produced, won = True, and the game tells the user 'You won' and displays the number of turns used and the number of cards remaining in the draw deck.
