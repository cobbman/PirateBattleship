*quick start -> in your terminal type: "python start.py"

|======================> WHAT THIS IS: <======================|
PirateBattleship is a 1-player game you play in your terminal (I hope to make it multi-player in the future). It's basically a simplified version of the popular "Battleship" game I used to play as a kid. I started it for fun, but mainly so I could learn about Object Oriented Programming with the Python language. I keep adding to this when I have free time, so please check back to see what's changed.

(note: I've only tested this game on Mac OSX and Ubuntu 12+, so I don't know how it works on Windows yet)

|======================> HOW TO PLAY: <======================|
1. Open your terminal and go to the directory you want the game to be in.
2. Clone the repo to your computer: git clone https://github.com/bigwilliam/PirateBattleship.git
3. Start the game with this command: python start.py

I hope you enjoy the game! Perhaps one day if I have the time I will create an online version of the game.

Comments or questions can be emailed to me: hello@bigwilliam.com


|======================> FILES: <======================|
start.py     - gathers info and creates the game object. Also initiates the runGame method on the game object
game.py      - creates a game object. Takes in the players, board, and boatList as arguments
boat.py      - creates a boat object
gameboard.py - creates a board object that can be different sizes (default is 10x10)
player.py    - creates a player. Right now the game is only 1 player


|======================> OTHER RANDOM NOTES TO MYSELF ARE BELOW: <======================|

To Do:
- validate inputs (regex), so if user makes an invalid move it won't break
- add feature to create boats of different sizes
- game.py endGame() line 109: when the boat coordinates are printed, they should be printed as the user sees them. i.e. 'J5' instead of (5,9)


Fixed:
- DONE: Add visual ASCII when boat is hit or miss to make it more fun (overall user experience needs improving)
- DONE AND RENAMED: clean up playgame.py - code there is messy
- DONE: AND SIMPLIFIED: some of the boats have negative coordinates… need to fix (boat.py)
- DONE: Update board draw method so it shows coordinate headers that the user can see
- DONE: put checks in place to make sure boats don't overlap!
- DONE: resolve the x,y vs y,x coordinates issue
- DONE: Board does not update the x,y coordinates coorectly. Boats show a hit, but board displays 'o' when coordinates are > 5

=========================================================================================================

FUNCTIONALITY:

Just some notes about how the game functions:

Normally coordinates on a graph are declared in the order x,y. But in Battleship, the user declares their move in the order y,x. For example, a player's move in Battleshihp might be "C4" - where "C" refers to the amount of rows DOWN (aka the 'y' axis) and "4" refers to the columns to the RIGHT (aka the 'x' axis), so they are being declared in reverse order.

So what is the correct way to prevent these from being mixed up?

1. We could just consider all coordinates in the classes to be in the order y,x. But the problem there would be that if the classes were to be used in another context, the y,x format would mess things up for them.

2. We could just take the user input, reverse it to match the "x,y" format and go from there, keeping all coordinate values in the classes as "x,y". The one problem is printing the gameboard so it displays rows and cols correctly, while still swapping x,y in the background for functionality.

2a. Actually, if we just consider everything to be in the order x,y and all we do is take the user input and swap it, everything else should be fine! But also when printing the board, we will have to swap values as well so it stays consistent with what the user should see. This should work.

I WILL USE #2a

