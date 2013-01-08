from __future__ import print_function # makes the print() function compatible with older versions of python
import string # lets us do some formatting for the draw method

class GameBoard:
    """(int, str)
    Create a square grid. Default is 10x10 with '.' as initial values.
    """
    def __init__(self, boardSize=10, setMark='.'):
        self.size = boardSize
        self.mark = setMark 
        self.grid = [ [ self.mark for row in range(self.size) ] for col in range(self.size) ]

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

    def updateHit(self, col, row, hitMark='x'):
        if self.grid[row][col] != self.mark:
            print("You already tried that, try something else.")
            return False # Already been played
        else:
            self.grid[row][col] = hitMark
            return True
            
    def updateMiss(self, col, row, missMark='o'):
        if self.grid[row][col] != self.mark:
            print("You already tried that, try something else.")
            return False # Already been played
        else:
            self.grid[row][col] = missMark
            return True
            
    def draw(self):
        rowHead = "ABCDEFGHIJ" # will be used as a reference for the player to see
        print("  0 1 2 3 4 5 6 7 8 9")
        for label, row in zip(rowHead, self.grid):
            print(label,end=" ")
            for col in row:
                print('{0:1}'.format(col), end=" ")
            print()

# for testing purposes
"""
board = GameBoard(10)
board.updateHit(3,4)
board.updateHit(2,1)
board.updateMiss(2,0)
board.updateMiss(2,2)
board.updateHit(5,3)
board.draw()
"""