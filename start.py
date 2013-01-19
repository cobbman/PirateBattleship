from __future__ import print_function
import player
import gameboard
import game 

#clear the screen
for i in range(50):
	print()

print ( "Pirate Battleship ASCII ART goes here. This game was made by Big William!" )
raw_input( "Press Enter to continue..." )

player = player.Player() # create the player object (options: playerName = '')
board = gameboard.GameBoard() # create the gameboard object (options: boardSize=10, setMark='.')

newGame = game.Game(player, board) # create and run the game 

newGame.runGame() # run the game object
