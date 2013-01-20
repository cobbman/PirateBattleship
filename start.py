from __future__ import print_function
import player
import gameboard
import game 

#clear the screen
for i in range(50):
	print()

print ( "Pirate Battleship ASCII ART goes here. This game was made by Big William!" )
raw_input( "Press Enter to continue..." )

player = player.Player() # create the player object for 1 player (options: playerName = '')
board = gameboard.GameBoard() # create the gameboard object (options: boardSize=10, setMark='.')

newGame = game.Game(player, board) # create a game object with player and board

newGame.runGame() # run the game object
