class Player:
    """ Creates a Player object. Good for future implementations when this game will become multiplayer"""

    def __init__(self, iName):
        self.name = iName
        self.score = 0
    
    def getName(self):
        return self.name

    def getScore(self):
        # will return the player's score (future use)
        return True

    def updateScore(self, points):
        return self.score + points


        
