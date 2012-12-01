readme.txt

Nov 30 - I'm going to make an ASCII console based battleship game in Python. It will be 1 player vs the computer. Only, the computer will be the only one with ships. The player just guesses his moves and the object of the game is to sink all the boats in the least amound of moves possible. Future editions may involve 2 or more players, or allow the player to also have ships that the computer can try to sink.

Elements of the game:
- driver: interacts with the humans and controls the game
- create board: makes the board
- track board: keeps track of the boats on the board (hidden to the user) and which have been hit
- check move: checks to see if the move is a hit or miss
- populate board: populates the board with boats
- intro: displays cool ASCII image of a boat with credits and maybe play some 8-bit sounds.
- config: a file to adjust configurations

Steps:
1. populate the board by randomly selecting boat locations, and boat direction. If the first random location will run off the board, then change the boat direction. If all 4 directions result in hitting a boat or running off the board, select a new location and repeat until all boats are placed
2. Ask the player to make a move
3. check the move, update the board display to show a hit or miss (most likely clear the console each time a move is made)
4. ask player for next move, or provide an "escape" entry to end game early

Options:
1. User can choose number of boats