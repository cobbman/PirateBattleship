from __future__ import print_function # makes the newer print() function compatible with older versions of python
import re # regex 
import displayArt # display art file

class Game:
    """ Plays the PirateBattleship game. The game itself is an object that takes these objects as arguments: player, board, and boatList """

    def __init__(self, iPlayers, iBoard, iListOfBoats):
        
        self.player = iPlayers
        self.board = iBoard
        self.boatList = iListOfBoats
        self.numberOfBoatsLeft, self.numberOfBoats = len(self.boatList), len(self.boatList)

        # reference coordinates from the player to the computer, just for internal use
        self.coordinateReference = { 'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9 }


    def runGame(self):
        """ This method runs the game """
        
        #### FIRST SET UP SOME HELPER FUNCTIONS ###
        
        def clearScreen(lines=50): # clears the screen by creating a bunch of newlines
            for i in range(lines):
                print()

        def getPlayerMove():
            """ Asks the player to make a move and returns the answer. I might want to split the input up inside this function rather than doing it outside """
            playerMove = raw_input("Yarr, Capt'n " + self.player.name + "! Make yer next move! => ")
            # It's possible that we should split the player move into xMove and yMove here instead of outside
            self.player.addToNumberOfMoves() # adds 1 to the number of moves the player makes
            return playerMove

        def moveHitsABoat(xCoord, yCoord, boatList):
            """ cycle through the boats and check to see if move is a hit or miss. Returns the boat that was hit, or False """
            for boat in boatList:
                if boat.isHit(xCoord,yCoord):
                    return boat
            return False

        def moveIsValid(playerMove):
            """ (str) -> bool

            Validate the move. Return True if valid, False if not. 
            Things to validate for:
            1. 2 characters in length only
            2. first is letter a-j, second is number 0-9
            3. move has not been played already
            THOUGHT: I'm thinking that the function getPlayerMove should handle this instead. aka combine this function with getPlayerMove.
            """

            # set up regex match
            validMove = re.compile("[a-j][0-9]") # Missing: Still need to check for length!
            if not validMove.match(playerMove):
                return False

            xMove = int(playerMove[1])
            yMove = int( self.coordinateReference[playerMove[0].upper()] )

            # check to be sure this move hasn't already been played, ask again if need be
            if self.board.hasAlreadyBeenPlayed(xMove,yMove):
                return False
            
            return True                

        # NOW WE'RE ACTUALLY PLAYING
        self.board.draw()
        while self.numberOfBoatsLeft > 0:
            
            newMove = getPlayerMove()

            ### CHECK IF MOVE IS VALID BEFORE CONTINUING
            while not moveIsValid(newMove):

                self.player.addToNumberOfMoves(moves = -1) # don't count the move because it is invalid

                print("Ye scallywag! Yer move ain't right! Did you already play that? Also, yer move must look like this: A5, got it?")

                newMove = getPlayerMove()

            # remember the user inputs coordinates as yx, but we need it to be xy, so here we do the switch
            xMove = int(newMove[1]) # [1] is the 2nd element of newMove
            yMove = int( self.coordinateReference[newMove[0].upper()] ) # [0] is the first element of newMove. convert letters to corresponding numbers we can use to update things with coordinates as int 

            

            # check to see if the move hits a boat   
            boatHit = moveHitsABoat(xMove, yMove, self.boatList) 

            if boatHit: # the move was a HIT
                boatHit.updateHit(xMove,yMove) # tell the boat to update coordinates with a hitMark
                self.board.updateHit(xMove,yMove) # tell the board to update coordinates with a hitMark
                displayArt.Hit()

                if boatHit.isSunk():
                    self.numberOfBoatsLeft = self.numberOfBoatsLeft - 1 # here's what the while loop is keeping track of
                    displayArt.Sunk()
                    raw_input( "Press Enter to continue..." )

            else: # The move was a MISS
                self.board.updateMiss(xMove,yMove)
                displayArt.Miss()

            print()
            self.board.draw()
            
            #TEST
            
            # print("For testing:")
            # print("Number of moves:", self.player.getNumberOfMoves() )
            # print("Player move translates to (" + str(xMove) + ", " + str(yMove) + ")")
            #for boat in self.boatList: # print all the boat coordinates so I can see them
            #    print( boat.getCoordinates() )
            print("Your last move was:", newMove)
            print("Number of boats left: ", self.numberOfBoatsLeft)

        return True # game completed successfully

    def endGame(self):

        totalMoves = int( self.player.getNumberOfMoves() )

        # calculate total spaces the boats occupied
        totalBoatSpaces = 0
        for boat in self.boatList:
            totalBoatSpaces += boat.getBoatSize()

        hitRatio = 100 * ( float(totalBoatSpaces) / float(totalMoves) )
        print()
        print("YOU WIN! Ye are a true Pirate Capt'n", self.player.name) 
        print("It took your sorry hide", totalMoves, "moves to win.") 
        print("You sunk", self.numberOfBoats, "boats, which had", totalBoatSpaces, "spaces!!!")
        print("Your HIT accuracy is:", "%.2f" % hitRatio, "percent!") 
        print("Here's the types of boats you sunk: ")
        for boat in self.boatList:
            print( "The" + boat.type + ", size " + str( boat.getBoatSize() ) + ". Located at " + str( boat.getCoordinates().keys() ) )

