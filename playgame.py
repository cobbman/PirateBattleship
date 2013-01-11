from __future__ import print_function # makes the newer print() function compatible with older versions of python
import boat # the boat class that creates boat objects
import gameboard # the gameboard class that creates the board object
import player # a player class for players objects

"""
How this will work:
The playGame class creates a Game object which handles everything from there within the object.
? => Should the playgame class be sent all the info it needs, or should it be allowed to ask for input first (i.e. asking the user how many boats they want in the game).
During game play, the user sets their name, and chooses how many boats they want to play against.
Then the user is shown the gameboard and is asked to make a move.
That move is then parsed and checked against the list of boat objects and the gameboard is updated accordingly as a hit or miss.
Each time the player makes a move, it is counted so that a score can be tallied in the end.
The boats know if they've been hit, if you send coordinates to them.
The gameboard keeps track of which locations have been played already, so the user can't play the same place twice.




"""

class playGame:
    """ Plays the PirateBattleship game """

    def __init__(self):
        
        self.player = player.Player() # create a player object
        self.board = gameboard.GameBoard() # create the board object!

        self.boatList = []

        # reference coordinates from the player to the computer
        self.coordinateReference = { 'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9 }
        


    def clearScreen(self, lines=50): # "clears" the screen in a primitive fashion
        for i in range(lines):
            print()

    def getPlayerMove(self):
        return raw_input("Arr, Capt'n " + player1.getName() + "! Make yer next move! => ")

    def checkMoveAgainstBoats(self, xCoord, yCoord, boatList):
        # cycle through the boats and check to see if move is a hit or miss
        for boat in boatList:
            if boat.isHit(xCoord,yCoord):
                boat.updateHit(xCoord,yCoord)
                board.updateHit(xCoord,yCoord)
                print("************ HIT **************")

                if boat.isSunk():
                    self.numberOfBoats = self.numberOfBoats - 1
                    print(" ^^^^^^^^^^^^ Ye SUNK a ship!!! ^^^^^^^^^^^^^^")
            else:
                board.updateMiss(xCoord,yCoord)
                print("--------------- MISS ---------------")

    def endOfGame(self):
        makeRoom()
        print("YOU WIN! Ye are a true Pirate Capt'n", player1.getName()) 
        board.draw()  
        print("It took your sorry hide ", player1.getNumberOfMoves(), "moves to win.") 
        hitRatio = len(boatList) * 3 / player1.getNumberOfMoves()
        print("Your accuracy is", hitRatio) 
        print("You sunk these boats:")
        for boat in boatList:
            print( "The", boat.type, "at", boat.getCoordinates() )


    


    ######################################################
    #
    #         Now we are ready to play the game!
    # 
    ######################################################

    def play(self):

        # INTRODUCTION
        print( "Pirate Battleship ASCII ART goes here. This game was made by Big William!" )
        raw_input( "Press Enter to continue..." )

        clearScreen(50)

        # GET PLAYER DETAILS AND BOATLIST
        self.player.setName( raw_input( "Welcome aboard Capt'n! What be yer name? " ) )
        self.numberOfBoats = int( raw_input( "How many boats do ye desire to sink today? (recommend 5) " ) )

        # CREATE THE LIST OF BOATS NOW THAT WE KNOW HOW MANY TO MAKE
        for num in range(self.numberOfBoats):
        newBoat = boat.Boat()
        if boatList > 0: # Check to make sure our newBoat doesn't overlap an existing boat
            while newBoat.checkIfBoatsOverlap(self.boatList):
                newBoat = boat.Boat()
        self.boatList.append(newBoat) # append our new boat to the boatList

        # for testing purposes, print the boat coordinates
        print("Created boat", num, "at these coordinates:", newBoat.getCoordinates().keys() )

        # NOW WE'RE ACTUALLY PLAYING
        while self.numberOfBoats > 0:
            #clearScreen()
            self.board.draw()
            newMove = getPlayerMove()
            yCoord = int( coordinateReference[newMove[0].upper()] )
            xCoord = int(newMove[1])

            while board.hasAlreadyBeenPlayed(xCoord,yCoord):
                print("Ye scallywag! Ye have already made that move! Try another!")
                newMove = getPlayerMove()
                yCoord = int(coordinateReference[newMove[0].upper()])
                xCoord = int(newMove[1])

            checkMoveAgainstBoats(xCoord,yCoord) # tells the user if HIT or MISS and updates board and boats accordingly

            player1.updateNumberOfMoves()
            
            #TEST
            print(newMove[0], "became", yCoord)
            print(newMove[1], "became", xCoord)
            print("Number of boats left: ", numberOfBoats)
            for boat in boatList:
                print(boat.getCoordinates())

        endOfGame()

