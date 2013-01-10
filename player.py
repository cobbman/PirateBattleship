class Player:
    """ Creates a Player object. """

    def __init__(self, playerName):
        self.name = playerName
        self.score = 0
        self.numberOfMoves = 0
    
    # get functions

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def getNumberOfMoves(self):
        return self.numberOfMoves

    # update functions

    def updateScore(self, points):
        self.score = self.score + points

    def updateNumberOfMoves(self, moves = 1):
        self.numberOfMoves += moves
