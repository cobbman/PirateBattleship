from __future__ import print_function # makes the newer print() function compatible with older versions of python
import boat # the boat class that creates boat objects
import gameboard # the gameboard class that creates the board object
import player # a player class for players objects


########################### 
#     helper stuff
###########################

# reference coordinates from the player to the computer
coordinateReference = { 'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9 }

# 'clears' the screen
def clearScreen():
    for i in range(50):
        print()

# make some room
def makeRoom():
    for i in range(5):
        print()

########################### 
#      introduction
###########################

print("Pirate Battleship ASCII ART goes here")

player1 = player.Player(raw_input("Welcome aboard Capt'n! What be yer name? "))
numberOfBoats = int(raw_input("How many boats do ye desire to sink today? (recommend 3) "))


###########################
#     create elements
###########################

board = gameboard.GameBoard()

boatList = [] # Boat coordinates are tuples as the keys and 'o' as initial values (when hit, value changes to 'x')

for num in range(numberOfBoats):
    newBoat = boat.Boat()

    print("Created boat", num, "at these coordinates:", newBoat.getCoordinates().keys())
    
    """
    # check to make sure newBoat doesn't overlap current boats
    #
    #
    #
    #
    THIS MIGHT NEED TO BE FIXED STILL
    for eachBoat in boatList:
        while (len(frozenset(newBoat.getCoordinates().keys()).intersection(eachBoat.getCoordinates().keys())) > 0):
            print("*** a boat overlapped, creating a new one ***")
            newBoat = boat.Boat()
    """
    # append our new boat to the boatList
    boatList.append(newBoat)


######################################################
#         Now we are ready to play the game!
######################################################

moveResult = '' # tells the user if it is a hit or not

def getPlayerMove():
    return raw_input("Arr, Capt'n " + player1.get_Name() + "! Make yer move! (example: C5) => ")

def checkMoveAgainstBoats(xCord, yCord):
    # cycle through the boats and check to see if move is a hit or miss
    for boat in boatList:
        if (xCord,yCord) in boat.getCoordinates():
            boat.isHit(xCord,yCord)
            board.updateHit(xCord,yCord)

            # after hitting the boat, check to see if it is sunk
            if boat.isSunk() == True:
                numberOfBoats -= 1
                print("Ye SUNK a ship!!!")

            moveResult = "xxxxxxxxxxxxxx HIT xxxxxxxxxxxxxx"
            break
    else:
        board.updateMiss(ns,ew)
        moveResult = "oooooooooo Miss ooooooooooooooo"


while numberOfBoats > 0:
    
    board.draw()
    if len(moveResult) > 0:
        print(moveResult)
    print('Boats Left:', numberOfBoats)
    move = ""

    # check the move and validate it
    while len(move) != 2:
        move = raw_input("Arr, make yer move Capt'n " + player1.get_Name() + "! (example: C4) => ")

    # convert move to int
    ns = int(coordinateReference[move[0].upper()])
    ew = int(move[1])

    checkMoveAgainstBoats(ew,ns)
    
    #TEST
    print(move[0], "became", ns)
    print(move[1], "became", ew)
    print("Number of boats left: ", numberOfBoats)
    for boat in boatList:
        print(boat.getCoordinates())

board.draw()    

print("YOU WIN! Ye are a true Pirate Capt'n", player1.getName()) 

makeRoom()


"""
1. The game starts, the user sees an intro screen (hits enter)
2. The board is created and boats positions randomly generated
3. asks for user name
4. Screen displays board and asks for input
5. input is checked for validity 
6. compare input with boat values
7. if found, update boat and board to 'x', run the "hit" screen for the user to see
8. if miss, update board to 'o', run the 'miss' screen
9. ask for next input
"""


"""
def showBoard():
	''' 
	Just displays what the board is supposed to look like
	'''
	print("  0 1 2 3 4 5 6 7 8 9")
	print("A . . . . . . . . . .")
	print("B . . . . . . . . . .")
	print("C . . . . . . . . . .")
	print("D . . . . . . . . . .")
	print("E . . . . . . . . . .")
	print("F . . . . . . . . . .")
	print("G . . . . . . . . . .")
	print("H . . . . . . . . . .")
	print("I . . . . . . . . . .")
	print("J . . . . . . . . . .")
#showBoard()
"""
