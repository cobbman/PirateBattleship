from __future__ import print_function
import player
import gameboard
import boat
import game 

"""
Gathers information and initiates the game object.

"""

def clearScreen(lines=50): #clear the screen
	for i in range(50):
		print()

def createBoatList(numBoats): # Create the list of boats
    """ (int -> list of dict) Returns a list of boats as dictionaries """

    # Having trouble deciding where this function/method should go. It doesn't quite fit in the board or boat object as a method the way I would like it to. I finally decided it belonged here, where the broader prespective is. This might change again as I tune things.
	def checkIfBoatsOverlap(boat, boatList): 
		""" (obj, list of obj) -> bool
		Returns True if boat.getCoordinates() overlaps any coordinate of boat in boatList """

		for eachBoat in boatList:
			boatCheck = set( eachBoat.getCoordinates() ) & set( boat.getCoordinates() )
			if len(boatCheck) > 0:
				# for testing purposes
				print("Our new boat", boat.getCoordinates().keys(), "overlaps a boat in our list at:", boatCheck)
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
        print("Created boat", num, "at these coordinates:", newBoat.getCoordinates().keys() )
        boatList.append(newBoat) # append our new boat to the boatList
    
    return boatList



### MAKE INTRODUCTIONS AND GATHER INFO WE NEED SO WE CAN START THE GAME

clearScreen()

print ( "Pirate Battleship ASCII ART goes here. This game was made by Big William!" )
raw_input( "Press Enter to continue..." )

clearScreen()

getName = raw_input( "Welcome aboard Capt'n! What be yer name? " )
numberOfBoats = int( raw_input( "Yarr! Captain", getName, "! How many boats do ye desire to sink today? (recommend 5) " ) )

listOfBoats = createBoatList(numberOfBoats)
player = player.Player(playerName=getName) # create the player object for 1 player (options: playerName = '')
board = gameboard.GameBoard() # create the gameboard object (options: boardSize=10, setMark='.')

newGame = game.Game(player, board, listOfBoats) # create a game object with player and board

if newGame.runGame(): # run the game! If it runs and finishes then end the game
	newGame.endGame() # play the end of game stats and messages
