from __future__ import print_function # makes the print() function compatible with older versions of python
import string # lets us do some formatting for the draw method

class GameBoard:
    """(int, str)
    Create a square grid. Default is 10x10 with '.' as initial values.
    """
    def __init__(self, setSize=10, setMark='.'):
        self.size = setSize
        self.mark = setMark 
        self.grid = [ [ self.mark for row in range(self.size)] for col in range(self.size) ]

    def getSize(self):
        return self.size

    def getMark(self):
        return self.mark

    def spacesLeft(self):
        # returns how many spaces have not been played yet
        count = 0
        for row in self.grid:
            for col in row:
                if self.mark in col:
                    count = count + 1
        return count

    def updateHit(self, row, col, hitMark='x'):
        if self.grid[row][col] != self.mark:
            return False # Already been played
        else:
            self.grid[row][col] = hitMark
            
    def updateMiss(self, row, col, missMark='o'):
        if self.grid[row][col] != self.mark:
            return False # Already been played
        else:
            self.grid[row][col] = missMark
            
    def draw(self):
        for row in self.grid:
            for col in row:
                print('{0:1}'.format(col), end=" ")
            print()

        """for x in range(1,11):
            print ('{0:1d} {1:3d} {2:5d}'.format(x, x*x, x*x*x))

        for x in range(1,11):
            print (repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
        """
"""
# for testing purposes
board = GameBoard(10)
board.updateHit(3,4)
board.updateHit(2,1)
board.updateMiss(2,0)
board.updateMiss(2,2)
board.updateHit(5,3)
board.draw()
"""
"""
How the game board display will work:
gameBoard will be an object that will be an array.
we will use dictionary values to match 'A' to 0, 'B' to 1, etc...
so that when the user makes a move, we can easily use
array[dict['A']][4] to identify the board location.
Then, we can update the array easily for showing the user.        
"""
