class Player:
    """ Creates a Player object. Good for future implementations when this game will become multiplayer. """

    def __init__(self, iName):
        self.name = iName
        self.score = 0
        self.numberOfMoves = 0
    
    # get functions

    def get_Name(self):
        return self.name

    def get_Score(self):
        return self.score

    def get_numberOfMoves(self):
        return self.numberOfMoves

    # update functions

    def update_Score(self, points):
        self.score = self.score + points

    def update_numberOfMoves(self, moves = 1):
        self.numberOfMoves += moves
