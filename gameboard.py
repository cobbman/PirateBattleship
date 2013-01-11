from __future__ import print_function # makes the print() function compatible with older versions of python
import string # lets us do some formatting for the draw method

class GameBoard:
    """ 
    Create a square grid as a list of lists. Default is 10x10 with '.' as initial values. 
    NOTE: Because the board stores values in the order of row then column, the x and y coordinates are switched to match.
    """
    
    def __init__(self, boardSize=10, setMark='.'):
        self.size = boardSize
        self.defaultMark = setMark 

        ### This creates the board ###
        self.grid = [ [ self.defaultMark for row in range(self.size) ] for col in range(self.size) ] 

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
            
    def draw(self): # this could be optimized more, especially since we're already using the string.format functions
        rowHead = "ABCDEFGHIJ" # will be used as a reference for the player to see
        print("  0 1 2 3 4 5 6 7 8 9")
        
        for label, row in zip(rowHead, self.grid):
            print(label,end=" ")
            for col in row:
                print('{0:1}'.format(col), end=" ")
            print()
