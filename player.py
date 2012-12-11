class Player:
    """ Creates a Player object. Good for future implementations when this game will become multiplayer"""

    def __init__(self, iName):
        self.playerName = iName
        self.playerScore = 0
    
    def name(self):
        return self.playerName

    def score(self):
        # will return the player's score (future use)
        return True

    def numberOfMoves(self):
        # will return the number of moves a player has made
        return True

    def boatsLeft(self):
        # will return number of boats not sunk
        return True

        
