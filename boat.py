import string
# in the future, Boat may need to know which board it is creatng the boat object for.
# so it can know the parameters of where to place the boat. For now, I'll assume a board of size 10x10
class Boat:
    """Create a boat object with specified length. Default length is 3. """
    def __init__(self, length=3, boardSize=10):
        self.length = length
        self.matrixLimit = boardSize

    def location(self):
        # sets an array of it's locaiton
    def isHit(self, x, y):
        #returns true if coordinates given is a hit, false if miss
    def isSunk(self):
        #returns true if the boat is sunk (all coordinates have been hit)
    def unitsLeft(self):
        # returns how many units are not hit
    def numberOfHits(self):
        # returns how many hits the boat has taken



