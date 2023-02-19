# Function to print out the board
def printBoard(board):
    # Iterate through the rows
    for row in board:
        # Print out the values in the curren row
        for i in range(3):
            # Not end of the row so print same line
            if i < 2:
                print(row[i] + " ", end = " ")
            else:
                # Last element print character and newline
                print(row[i])

# Function performs game
def playGame(board):
    # Print the inital board
    printBoard(board)

    

def main():
    # Creat our board
    board = [["*", "*", "*"],
             ["*", "*", "*"],
             ["*", "*", "*"]]
    # Start our game
    playGame(board)

main()