from __future__ import print_function # makes the print() function compatible with older versions of python
import string # lets us do some formatting for the draw method

class GameBoard:
    """ 
    Create a square grid as a list of lists. Default is 10x10 with '.' as initial values. 
    NOTE: Because the board stores values in the order of row then column (y then x), the x and y coordinates are switched to match. Outside this class everything is considered to be x,y (col, row)
    """
    
    def __init__(self, boardSize=10, setMark='.'):
        self.size = boardSize
        self.defaultMark = setMark 

        ### This creates the board ###
        self.grid = [ [ self.defaultMark for row in range(self.size) ] for col in range(self.size) ] 


    def checkIfBoatsOverlap(self, boat, boatList):
        """ (obj, list of obj) -> bool
        Returns True if boat.getCoordinates() overlaps any coordinate of boat in boatList """
        for eachBoat in boatList:
            self.boatCheck = set( eachBoat.getCoordinates() ) & set( boat.getCoordinates() )
            if len( self.boatCheck ) > 0:
                return True # the boat overlaps one already in the list
        return False # the boat does not overlap, it's all good!

    def hasAlreadyBeenPlayed(self, xCoord, yCoord):
        # returns True if the user has already made a move at (xCoord,yCoord)
        return not self.grid[yCoord][xCoord] == self.defaultMark

    def countSpacesNotPlayed(self):
        count = 0
        for row in self.grid:
            for space in row:
                if self.defaultMark in space:
                    count = count + 1
        return count

    def updateHit(self, xCoord, yCoord, hitMark='x'):
            self.grid[yCoord][xCoord] = hitMark
            
    def updateMiss(self, xCoord, yCoord, missMark='o'):
            self.grid[yCoord][xCoord] = missMark
            
    def draw(self): # Draws the board for the user to see. The most commonly used method of this class.
        rowLabels = "ABCDEFGHIJ" # will be used as a reference for the player to see

        print("  0 1 2 3 4 5 6 7 8 9") # references for the columns
        for rowLabel, row in zip(rowLabels, self.grid): # zip lets us iterate through two variables at the same time
            print(rowLabel,end=" ") # print rowLabel but don't start a newline, yet.
            for col in row:
                print('{0:1}'.format(col), end=" ") # print each board coordinate and keep it evenly spaced
            print() # now that we printed a row completely, start a newline
