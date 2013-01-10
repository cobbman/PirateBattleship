from __future__ import print_function # makes the newer print() function compatible with older versions of python
import boat # the boat class that creates boat objects
import gameboard # the gameboard class that creates the board object
import player # a player class for players objects


########################### 
#     helper functions
###########################

# reference coordinates from the player to the computer
coordinateReference = { 'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9 }

def boatsOverlap(num, newBoat, boatList):
    """ Checks to see if the newBoat overlaps coordinates of boats already in the boatList """
    for eachBoat in boatList:
        boatCheck = set( eachBoat.getCoordinates() ) & set( newBoat.getCoordinates() )
        if len( boatCheck ) > 0:
            print("Our new boat", num, newBoat.getCoordinates().keys(), "overlaps a boat in our list at:", boatCheck)
            return True
    return False

# "clears" the screen in a primitive fashion
def clearScreen():
    for i in range(50):
        print()

# make some room by adding spaces
def makeRoom():
    for i in range(5):
        print()

moveResult = '' # tells the user if it is a hit or not

def getPlayerMove():
    return raw_input("Arr, Capt'n", player1.getName(), "! Make yer next move!", player1.getNumberOfMoves(), "moves so far => ")

def checkMoveAgainstBoats(xCoord, yCoord):
    # cycle through the boats and check to see if move is a hit or miss
    for boat in boatList:
        if boat.isHit(xCoord,yCoord):
            boat.updateHit(xCoord,yCoord)
            board.updateHit(xCoord,yCoord)
            print("************ HIT **************")

            # after hitting the boat, check to see if it is sunk
            if boat.isSunk():
                numberOfBoats -= 1
                print("Ye SUNK a ship!!!")
        else:
            board.updateMiss(xCoord,yCoord)
            print("--------------- MISS ---------------")

def endOfGame():
    makeRoom()
    print("YOU WIN! Ye are a true Pirate Capt'n", player1.getName()) 
    board.draw()    
    print("You sunk these boats:")
    for boat in boatList:
        print( "The", boat.type, "at", boat.getCoordinates() )



########################### 
#      introduction
###########################

clearScreen()

print( "Pirate Battleship ASCII ART goes here. This game was made by Big William!" )
raw_input( "Press Enter to continue..." )

clearScreen()

player1 = player.Player( raw_input( "Welcome aboard Capt'n! What be yer name? " ) )
numberOfBoats = int( raw_input( "How many boats do ye desire to sink today? (recommend 3) " ) )


###########################
#     create elements
###########################

board = gameboard.GameBoard() # create the board!

boatList = [] # Create an empty list of boats!

# Create as many boats as was requested!
for num in range(numberOfBoats):
    newBoat = boat.Boat()
    if boatList > 0: # Check to make sure our newBoat doesn't overlap an existing boat
        while boatsOverlap(num, newBoat, boatList):
            newBoat = boat.Boat()

    # append our new boat to the boatList
    boatList.append(newBoat)

    # for testing purposes, print the boat coordinates
    print("Created boat", num, "at these coordinates:", newBoat.getCoordinates().keys() )


######################################################
#
#         Now we are ready to play the game!
# 
######################################################

while numberOfBoats > 0:
    #clearScreen()
    board.draw()
    
    newMove = getPlayerMove()
    # convert move to int so we can easily pass it around
    yCoord = int(coordinateReference[newMove[0].upper()])
    xCoord = int(newMove[1])

    checkMoveAgainstBoats(xCoord,yCoord)

    player1.updateNumberOfMoves()
    
    #TEST
    print(newMove[0], "became", yCoord)
    print(newMove[1], "became", xCoord)
    print("Number of boats left: ", numberOfBoats)
    for boat in boatList:
        print(boat.getCoordinates())

endOfGame()

