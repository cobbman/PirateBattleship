class Player:
    """ Creates a Player object. """

    def __init__(self, playerName=''):
        self.name = playerName
        self.score = 0
        self.numberOfMoves = 0


    def setName(self, newName):
        self.name = newName

    def getScore(self):
        return self.score

    def getNumberOfMoves(self):
        return self.numberOfMoves

    def updateScore(self, points):
        self.score = self.score + points

    def addNumberOfMoves(self, moves = 1):
        self.numberOfMoves += moves
