from __future__ import print_function
import player
import gameboard
import boat
import game 


"""
How this will work:
start.py gathers information such as player name and how many boats they want to sink. Then creates a Game object which runs the game.

Then the user is shown the gameboard and is asked to make a move.
That move is then parsed and checked against the list of boat objects and the gameboard is updated accordingly as a hit or miss.
The updated board is reprinted on the screen and the user is asked to move again.
Each time the player makes a move, it is counted so that a score can be tallied in the end.
The boats know whether they've been hit, if you send coordinates to them.
The gameboard keeps track of which locations have been played already, so the user can't play the same place twice.

* NOTE: the boat coordinates are separate from the gameboard coordinates, but both get updated at the same time.

* NOTE: the gameboard is only for the user to see. As far as the game is concerned, the board only keeps track of which coordinates have been played. The boat coordinates are where the game keeps track of hits/misses.


"""

def clearScreen(lines=50): #clear the screen
	for i in range(50):
		print()

def createBoatList(numBoats): # Creates the list of boats
	""" (int -> list of dict) Returns a list of boats as dictionaries """

	# Having trouble deciding where this function/method should go. It doesn't quite fit in the board or boat object as a method the way I would like it to. I finally decided it belonged here, where the broader prespective is. This might change again as I tune things.
	def checkIfBoatsOverlap(boat, boatList): 
		""" (obj, list of obj) -> bool
		Returns True if boat.getCoordinates() overlaps any coordinate of boat in boatList """

		for eachBoat in boatList:
			boatCheck = set( eachBoat.getCoordinates() ) & set( boat.getCoordinates() )
			if len(boatCheck) > 0:
				# for testing purposes
				#print("Our new boat", boat.getCoordinates().keys(), "overlaps a boat in our list at:", boatCheck)
				return True # the boat overlaps one already in the list
		return False # the boat does not overlap, it's all good!
    
	boatList = []
	# Count through and create the boats
	for num in range(numBoats):
		newBoat = boat.Boat()
		if len(boatList) > 0: # Check to make sure our newBoat doesn't overlap an existing boat
			while checkIfBoatsOverlap(newBoat, boatList):
				newBoat = boat.Boat()
		# for testing purposes, print the boat coordinates
		#print("Created boat", num, "at these coordinates:", newBoat.getCoordinates().keys() )
		boatList.append(newBoat) # append our new boat to the boatList
    
	return boatList



### MAKE INTRODUCTIONS AND GATHER INFO WE NEED SO WE CAN START THE GAME

clearScreen()

print ( "Pirate Battleship ASCII ART goes here. This game was made by Big William!" )
print ( "This game is still in production, so things aren't all finished yet." )
print ( "Hopefully that won't be too annoying. You can always change some code if you like :)")
print ( "If you have any comments drop me a line: hello@bigwilliam.com")
print ( "Have Fun!!!")
raw_input( "Press Enter to continue..." )

clearScreen()

getName = ''
while getName == '':
	getName = raw_input( "Welcome aboard Capt'n! What be yer name? " )

numberOfBoats = 0
while numberOfBoats < 1 or numberOfBoats > 25:
	numberOfBoats = int( raw_input( "Yarr Cap'n " + getName + ", how many boats do ye desire to sink today? (recommend 5-15. The more boats the easier, but don't go over 25) " ) )

listOfBoats = createBoatList(numberOfBoats)
player = player.Player(playerName=getName) # create the player object for 1 player (options: playerName = '')
board = gameboard.GameBoard() # create the gameboard object (options: boardSize=10, setMark='.')

newGame = game.Game(player, board, listOfBoats) # create a game object with player and board

if newGame.runGame(): # run the game! If it runs and finishes then end the game
	newGame.endGame() # play the end of game stats and messages
