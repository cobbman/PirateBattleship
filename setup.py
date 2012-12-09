# This file creates the board and the boats on that board
from random import randint

def board():
	'''
	Returns  a dictionary of 100 keys representing spaces on the board. Keys are tuples, and the starting values are all "."
	'''
	rowHeader = "0123456789"
	colHeader = "ABCDEFGHIJ"
	board = {}

	for i in rowHeader:
		for j in rowHeader:
			board[(i,j)] = "."
	return board

# create the board, but as an array
def boardArray():
	'''
	Returns a list of lists 10x10 with "." in each value
	'''
	return [ [ "." for row in range(10)] for col in range(10) ] #create the board with  "." only
	

# create the boat locations on the board
def boats(numBoats):
	'''(int -> dict)
	Returns a dictionary of boats with their locations on the board.
	To keep it simple at first, boats will only be 3 spaces long. In the future I'll make it so some are different lengths.
	'''
	boat = []
	boats = []
	for i in range(numBoats): 
		x = randint(0,9) # east, west
		y = randint(0,9) # north, south
		
		
		# check to make sure the boat doesn't run off the board, if it does, regenerate the direction and try again
		
		def verifyLocation():
			d = randint(0,3) # 0 = north, 1 = east, 2 = south, 3 = west
			# NEED TO CHECK TO MAKE SURE BOATS DON'T OVERLAP
			if (d == 0 and y-2 < 0) or (d == 1 and x+2 > 9) or (d == 3 and y+2 > 9) or (d == 4 and x-2 < 0):
				verifyLocation()
			return d
		d = verifyLocation()

		if d == 0:
			boat = [[x,y],[x,y-1],[x,y-2]] # if facing north
		if d == 1:
			boat = [[x,y],[x+1,y],[x+2,y]] # if facing east
		if d == 2:
			boat = [[x,y],[x,y+1],[x,y+2]] # if facing south
		if d == 3:
			boat = [[x,y],[x-1,y],[x-2,y]] # if facing west
		boats[len(boats):] = boat
	return boats


	

