from random import randint

class Boat:
    """Create a boat object with specified length. Default length is 3. Prereq: boardSize is > boatLength"""
    
    def __init__(self, boatLength=3, boardSize=10):
        self.length = boatLength
        self.matrixLimit = boardSize
        self.coordinates = {} # declare and empty dict used for the boat coordinates later on
        self.hitMark  = 'x'
        self.missMark = 'o'


        boatDirection = randint(0,1) # random direction the boat will be facing. 0 is vert, 1 is horiz
        # Creating the boat coordinates now based on what direction it's facing.
        # x counts to the right, y counts down (i.e. on a graph, we're in Q4) 
        # The keys will be tuples of the coordinates; default values are set to the missMark

        if boatDirection == 0: # if direction is verticle (0) add to the y coordinates
            # randomly choose the starting point, but limit to the size of the board
            x = randint(0, self.matrixLimit - 1)
            y = randint(0, self.matrixLimit - self.length) # use self.length so it won't run off the board
            for i in range(self.length):
                self.coordinates[(x,y)] = self.missMark
                y = y + 1

        # if direction is horizontal (1) add to the x coordinates     
        if boatDirection == 1:
            # randomly choose the starting point, but limit to the size of the board
            x = randint(0, self.matrixLimit - 1)
            x = randint(0, self.matrixLimit - self.length) # use self.length so it won't run off the board
            y = randint(0, self.matrixLimit - 1)
            for i in range(self.length):
                self.coordinates[(x,y)] = self.missMark
                x = x + 1
    
    def getCoordinates(self):
        return self.coordinates
    
    def isHit(self, ns, ew):
        #returns true and updates boat value if coordinates given is a hit, false if miss or coordinate already played
        if (ns,ew) not in self.coordinates:
            return False
        elif self.coordinates[(ns,ew)] == self.hitMark:
            return False
        else:
            self.coordinates[(ns,ew)] = self.hitMark
            return True
        
    def isSunk(self):
        #returns true if the boat is sunk (all coordinates have been hit)
        return not (self.missMark in self.coordinates.values())
    
    def numberMissed(self):
        # returns how manns coords have not been hit nset
        count = 0
        for key in self.coordinates:
            if self.coordinates[key] == self.missMark:
                count = count + 1
        return count

    def numberOfHits(self):
        # returns how many hits the boat has taken
        count = 0
        for key in self.coordinates:
            if self.coordinates[key] == self.hitMark:
                count = count + 1
        return count

""" FOR TESTING PURPOSES """
#boat1 = Boat(3)
#print(boat1.getCoordinates())
#boat2 = Boat(4)
#print(boat2.getCoordinates())
#boat3 = Boat(5)
#print(boat3.getCoordinates())


