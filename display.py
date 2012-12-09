# display.py
# responsible for making viewer-friendly versions of the board

def showBoard(board):
    '''
    Takes a list of lists and prints the value in a user-friendly way.
    This includes showing the row/col header values
    '''
    #print the header
    print("  0  1  2  3  4  5  6  7  8  9 ")
    # print the board
    colHeader = "ABCDEFGHIJ"
    for row in board:
        print('A ', end='')
        for item in row:
            print(item, " ", end='')
        print()
    
