from __future__ import print_function # makes the print() function compatible with older versions of python
import boat
import gameboard
import player

########################### 
#      introduction
###########################
print("Yarr Pirate Battleship matey!")
player1 = player.Player(raw_input("What be yer name? "))
theBoardSize = int(raw_input("How large a board? (recommend 10)"))
numBoats = int(raw_input("How many boats? (recommend 3)"))

###########################
#     create elements
###########################

# create the board
board = gameboard.GameBoard(theBoardSize)

# create the boats. Boat coordinates are dictionaries with tuples as the coordinates and 'o' as the initial values (when hit, value changes to 'x')
boatList = []
for num in range(numBoats):
    newBoat = boat.Boat(boardSize=theBoardSize)
    boatList.append(newBoat.getCoordinates())

#test the boats
print("The boat list is:")
print(boatList)




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
