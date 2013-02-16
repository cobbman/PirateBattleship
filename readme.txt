readme.txt

This game finished, so you can play it! But, it still needs a few things done
to make the game play better. 

Comments or questions can be emailed to me: hello@bigwilliam.com

If you want to try it for what I have so far, run in your terminal: python start.py

Files:
start.py - gathers info and creates the game object. Also initiates the runGame method on the game object
game.py - creates a game object. Takes in the players, board, and boatList as arguments
boat.py - boat class, creates a boat object
gameboard.py - creates a board object that can be different sizes (default is 10x10)
player.py - creates a player. Right now the game is only 1 player


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

3. Actually, if we just consider everything to be in the order x,y (column,row), and all we do is take the user input and swap it, everything else should be fine! But also when printing the board, we will have to swap values as well so it stays consistent with what the user should see.

I WILL USE #3

