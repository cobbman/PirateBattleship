import setup
import display

# introduction
print("Yarr Pirate Battleship matey!")
name = input("What be yer name? ")
print("Hello", name)

# setup the board and boats
board = setup.board()
boardArray = setup.boardArray()
boats = setup.boats(5) #takes the number of boats as an argument

# display the board for the user
displayBoard = display.showBoard(boardArray)

# begin play
boats_left = 5
while boat_left > 0:
        move = prompt("Make your move: ")

        #check to see if it's a hit or miss and notify the user

        # update and re-display the board

        # Steps of how the game will work
'''
1. The game starts, the user sees an intro screen (hits enter)
2. The board is created and boats positions randomly generated
3. asks for user name
4. Screen displays board and asks for input
5. input is checked for validity 
6. compare input with boat values
7. if found, update boat and board to 'x', run the "hit" screen for the user to see
8. if miss, update board to 'o', run the 'miss' screen
9. ask for next input
'''



# for starters, I'm going to create a board to see what it's supposed to look like
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

#note: "x" will be hit mark, "o" will be a miss mark and "." is default

# Next, I want to create the board as a matrix so that it can be manipulated in the game



	# now we will create the header values (numbers 0-9) and preserve the spacing
	#board[0][0] = " "
	#for num in range(10):
	#	board[0][num + 1] = " " + str(num)

	#print it so we can test it
	#for row in board:
	#	print(row)
#createBoardArray()


# Another idea for displaying the board is to exclude the row/col headers completely from the board itself and only insert them when the board is being displayed. This way I can keep the board arrays pure without worring about header values (which should not be edited).
# Also, when displaying the board, maybe I won't keep the spaces in the array values either, and just insert those when displaying itu

# An idea for controlling the board in the background is to use a dictionary to store the values. This might be a good idea actually, because I can use keys to reference and update the board if it's a hit or miss or "."





