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

def createBoard():
	'''
	Create the board using an array matrix
	'''
	board = [ [ "." for row in range(10)] for col in range(10) ] #create the board with  " ." only

	# headers are for display purposed only and won't be included in the board matrix
	rowHeader = "0123456789"
	colHeader = "ABCDEFGHIJ"

	# now we will create the header values (numbers 0-9) and preserve the spacing
	#board[0][0] = " "
	#for num in range(10):
	#	board[0][num + 1] = " " + str(num)

	#print it so we can test it
	#for row in board:
	#	print(row)
createBoard()


# Another idea for displaying the board is to exclude the row/col headers completely from the board itself and only insert them when the board is being displayed. This way I can keep the board arrays pure without worring about header values (which should not be edited).
# Also, when displaying the board, maybe I won't keep the spaces in the array values either, and just insert those when displaying it

###

# An idea for controlling the board in the background is to use a dictionary to store the values. This might be a good idea actually, because I can use keys to reference and update the board if it's a hit or miss or "."
boardAsDictionary = { (A, 0):".", (A, 1):".", (A, 2):".", (A, 3):"." } # and so forth

def createDictBoard():
	'''
	going to create the board as a dictionary
	'''
	





