from __future__ import print_function # makes the print() function compatible with older versions of python
import boat
import gameboard
import player

########################### 
#      introduction
###########################
print("Yarr Pirate Battleship matey!")
player1 = player.Player(raw_input("What be yer name? "))
#theBoardSize = int(raw_input("How large a board? (recommend 10)"))
theBoardSize = 10 # right now the board size must be 10 to keep 'coordinateReference' simple
numBoats = int(raw_input("How many boats do ye desire to sink today? (recommend 3)"))

###########################
#     create elements
###########################

# create a dictionary for referencing coordinates from the player to the computer
coordinateReference = { 'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9 }

# create the board
board = gameboard.GameBoard(theBoardSize)

# create the boats. Boat coordinates are dictionaries with tuples as the coordinates, and 'o' as the initial values (when hit, value changes to 'x')
boatList = []
for num in range(numBoats):
    newBoat = boat.Boat(boardSize=theBoardSize)
    # now we're going to compare the boat we just made to the list of boats - making sure it doesn't overlap them
    for key in newBoat.getCoordinates():
        while key in boatList: # if any of the coordinates show up in current boatList, remake the newBoat and keep checking until it doesn't show up in boats already made
            print("found boat in list, regenerating a new boat.")
            newBoat = boat.Boat(boardSize=theBoardSize)
    # once the boat has been compared
    boatList.append(newBoat)

###########################
#     Play the game!
###########################
def clearScreen():
    for i in range(5):
        print()

while numBoats > 0:
    clearScreen()
    board.draw()
    print('Boats Left:', numBoats)
    move = raw_input("Arr, make yer move " + player1.name() + "! (example: C4)")

    # convert move to int format (note x and y coords are reversed cuz in Battleship the letter is the row, yadda yadda, oops)
    ns = int(coordinateReference[move[0].upper()])
    ew = int(move[1])

    # check to see if move is a hit or miss
    for boat in boatList:
        if (ns,ew) in boat.getCoordinates():
            boat.isHit(ns,ew)
            board.updateHit(ns,ew)
            # after hitting the boat, check to see if it is sunk
            if boat.isSunk() == True:
                numBoats = numBoats - 1
            print()
            print("xxxxxxxxxxxxxxx Boat was hit! xxxxxxxxxxxxxx")
            print("xxxxxxxxxxxxxxx Boat was hit! xxxxxxxxxxxxxx")
            print("xxxxxxxxxxxxxxx Boat was hit! xxxxxxxxxxxxxx")
            print()
            break
    else:
        board.updateMiss(ns,ew)
        print()
        print("oooooooooo Miss ooooooooooooooo")
        print("oooooooooo Miss ooooooooooooooo")
        print("oooooooooo Miss ooooooooooooooo")
        print()
    
    #TEST
    print(move[0], "became", ns)
    print(move[1], "became", ew)
    print("Number of boats left: ", numBoats)
    for boat in boatList:
        print(boat.getCoordinates())

clearScreen()
board.draw()    
print("Game is over. Ye are a true Pirate!") 
for i in range(5):
    print()


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
