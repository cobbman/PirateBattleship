from __future__ import print_function # makes the newer print() function compatible with older versions of python

"""
How this will work:
start.py creates a Game object which handles everything from there within the object.
During game play, the user sets their name, and chooses how many boats they want to play against.
Then the user is shown the gameboard and is asked to make a move.
That move is then parsed and checked against the list of boat objects and the gameboard is updated accordingly as a hit or miss.
The updated board is reprinted on the screen and the user is asked to move again.
Each time the player makes a move, it is counted so that a score can be tallied in the end.
The boats know whether they've been hit, if you send coordinates to them.
The gameboard keeps track of which locations have been played already, so the user can't play the same place twice.
* NOTE: the boat coordinates are separate from the gameboard coordinates, but both get updated at the same time.

? => Should the playgame class be sent all the info it needs, or should it be allowed to ask for input first (i.e. asking the user how many boats they want in the game).
AA => The playGame class will create a game object AFTER the info is gathered from the user about the game.


"""

class Game:
    """ Plays the PirateBattleship game """

    def __init__(self, iPlayers, iBoard, iListOfBoats):
        
        self.player = iPlayers
        self.board = iBoard
        self.boatList = iListOfBoats
        self.numberOfBoats = len(self.boatList)

        # reference coordinates from the player to the computer
        self.coordinateReference = { 'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9 }


    def runGame(self):
        #### FIRST SET UP SOME HELPER FUNCTIONS ###
        
        def clearScreen(lines=50): # clears the screen by creating a bunch of newlines
            for i in range(lines):
                print()

        def getPlayerMove():
            playerMove = raw_input("Yarr, Capt'n " + self.player.getName() + "! Make yer next move! => ")
            self.player.addToNumberOfMoves() # count how many moves are made
            return playerMove

        def moveHitsABoat(xCoord, yCoord, boatList):
            # cycle through the boats and check to see if move is a hit or miss
            for boat in boatList:
                if boat.isHit(xCoord,yCoord):
                    return boat
            return False


        # NOW WE'RE ACTUALLY PLAYING
        self.board.draw()
        while self.numberOfBoats > 0:
            
            newMove = getPlayerMove()

            # remember the user inputs coordinates as yx, but we need it to be xy, so here we do the switch
            xMove = int(newMove[1])
            yMove = int( coordinateReference[ newMove[0].upper() ] ) # convert letters to corresponding numbers we can use to update things with coordinates as int 

            # check to be sure this move hasn't already been played, ask again if need be
            while board.hasAlreadyBeenPlayed(xMove,yMove):
                print("Ye scallywag! Ye have already made that move! Try another!")
                newMove = getPlayerMove()
                xMove = int(newMove[1])
                yMove = int( coordinateReference[ newMove[0].upper() ] )

            # check to see if the move hits a boat   
            boatHit = moveHitsABoat(xMove, yMove, self.boatList):
            if boatHit:
                boatHit.updateHit(xMove,yMove)
                board.updateHit(xMove,yMove)
                print("xxxxxxxxxxxxxxxxxxxxxx HIT xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                
                if boatHit.isSunk():
                    self.numberOfBoats = self.numberOfBoats - 1 # here's what the while loop is keeping track of
                    print(" ^^^^^^^^^^^^ Ye SUNK a ship!!! ^^^^^^^^^^^^^^")
            else:
                board.updateMiss(xCoord,yCoord)
                print("ooooooooooooooooooooo MISS ooooooooooooooooooooooooooooo")

            self.board.draw()
            #TEST
            print("For testing:")
            print(newMove[0], "became", yCoord)
            print(newMove[1], "became", xCoord)
            print("Number of boats left: ", self.numberOfBoats)
            for boat in boatList:
                print( boat.getCoordinates() )

        return True # game completed successfully

    def endGame(self):

        totalMoves = self.player.getNumberOfMoves()
        hitRatio = len(self.boatList) / totalMoves

        board.draw()
        print("YOU WIN! Ye are a true Pirate Capt'n", self.player.getName()) 
        print("It took your sorry hide ", totalMoves, "moves to win.") 
        
        print("Your accuracy is:", hitRatio) 
        print("You sunk", len(self.boatList), "boats!!!")
        print("Here's the types of boats you sunk: ")
        for boat in boatList:
            print( "The", boat.type, " size", boat.getBoatSize(), "located at", boat.getCoordinates() )

