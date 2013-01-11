from random import randint

class Boat:
    """Create a boat object with specified length. Default length is 3. Prereq: boardSize is > boatLength"""
    
    def __init__(self, boatLength=3, boardSize=10):
        self.name = ''
        self.length = boatLength
        self.type = ''
        self.matrixLimit = boardSize
        self.coordinates = {} # coordinates will relate to boat's hit or miss status
        self.hitMark  = 'x'
        self.missMark = 'o'

        # set the boat type based on boat length
        boatTypes = { 2:"Sloop", 3:"Brigantine", 4:"Warship", 5:"Squarerigger" }
        if self.length:
            self.type = boatTypes[self.length]

        ### SET THE BOAT COORDINATES ###
        boatDirection = randint(0,1) # Set boat direction: 0 is vertical and 1 is horizontal

        if boatDirection == 0: # if direction is vertical (0) add to the y coordinates
            x = randint(0, self.matrixLimit - 1)
            y = randint(0, self.matrixLimit - self.length) # use self.length so it won't run off the board
            for i in range(self.length):
                self.coordinates[(x,y)] = self.missMark
                y = y + 1
             
        if boatDirection == 1: # if direction is horizontal (1) add to the x coordinates
            x = randint(0, self.matrixLimit - self.length) # use self.length so it won't run off the board
            y = randint(0, self.matrixLimit - 1)
            for i in range(self.length):
                self.coordinates[(x,y)] = self.missMark
                x = x + 1
    
    def getCoordinates(self):
        return self.coordinates
    
    def isHit(self, xCoord, yCoord):
        """ Returns True if coordinates given are found in the boat. Returns False if miss. """ 
        return (xCoord,yCoord) in self.coordinates

    def updateHit(self, xCoord, yCoord):
        """ Update the boat with a hitMark at the given coordinates """
        self.coordinates[(xCoord,yCoord)] = self.hitMark
        
    def isSunk(self):
        """ Returns true if the boat is sunk (all coordinates have been hit) """
        return not (self.missMark in self.coordinates.values())
    
    def getNumberOfHits(self):
        """ Returns how many hits the boat has taken """
        count = 0
        for key in self.coordinates:
            if self.coordinates[key] == self.hitMark:
                count = count + 1
        return count

    def getNumberMissed(self):
        """ Returns how many coordinates have not been hit yet """
        count = 0
        for key in self.coordinates:
            if self.coordinates[key] == self.missMark:
                count = count + 1
        return count

    def checkIfBoatsOverlap(self, boatList):
        """ (list of obj) -> bool
        Returns True if self.coordinates overlaps any coordinate of boat in boatList """
        for eachBoat in boatList:
            boatCheck = set( eachBoat.getCoordinates() ) & set( self.coordinates )
            if len( boatCheck ) > 0:
                # for testing purposes
                print("Our new boat", self.coordinates.keys(), "overlaps a boat in our list at:", boatCheck)
                return True
        return False
