from random import randint
# Our boat will have to take boardSize as a parameter to know what it's limits are.
# For now, I'll assume a default board of size 10x10
class Boat:
    """Create a boat object with specified length. Default length is 3. """
    def __init__(self, boatLength=3, boardSize=10):
        self.length = boatLength
        self.matrixLimit = boardSize
        self.coords = {}

        # randomly choose coordinates where the boat will start from
        x = randint(0, self.matrixLimit - 1)
        y = randint(0, self.matrixLimit - 1)       

        def setDirection(self):
            d = randint(0,3)  # 0 = north, 1 = east, 2 = south, 3 = west
            # check to make sure that the boat won't run off the board
            if (d == 0 and y-(self.length-1) < 0) or (d == 1 and x+(self.length-1) > 9) or (d == 3 and y+(self.length-1) > 9) or (d == 4 and x-(self.length-1) < 0):
                setDirection()
            return d
        d = setDirection()

        if d == 0: # if facing NORTH
            for i in range(self.length):
                self.coord[(x,y)] = 'o'
                y = y - 1
        if d == 1: # if facing EAST
            for i in range(self.length):
                self.coord[(x,y)] = 'o'
                x = x + 1
        if d == 2: # if facing SOUTH
            for i in range(self.length):
                self.coord[(x,y)] = 'o'
                y = y + 1
        if d == 3: # if facing WEST
            for i in range(self.length):
                self.coord[(x,y)] = 'o'
                x = x - 1

        return self.coords
        
    def isHit(self, x, y):
        #returns true if coordinates given is a hit, false if miss
    def isSunk(self):
        #returns true if the boat is sunk (all coordinates have been hit)
    def unitsLeft(self):
        # returns how many units are not hit
    def numberOfHits(self):
        # returns how many hits the boat has taken



