from random import randint

def create_board():
	'''
	going to create the board as a dictionary where the keys are tuples
	'''
	rowHeader = "0123456789"
	colHeader = "ABCDEFGHIJ"
	global board = {}

	for i in colHeader:
		for j in rowHeader:
			board[(i,j)] = "."

def create_boats():
	'''
	Randomly generates coordinates on the board and determines the locations of the boats
	5 boats:
	1. two
	2. three
	3. three
	4. four
	5. five
	'''
	randint(0,9)

	

