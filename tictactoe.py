# Place the designated piece at the specified spot
def updateBoard(row, column, board, piece):
    # Update the board
    board[row][column] = piece
    # Print the board
    printBoard(board)
    # Return the updated board
    return board

def validInput(row, column, board):
    # Check if the space is already occupied
    if board[row][column] == "X" or board[row][column] == "O":
        return False
    return True

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
    # Ask user for their move
    row = int(input("What row do you want to place your piece: "))
    column = int(input("What column do you want to place your piece: "))
    # Check if the move is valid
    while validInput(row, column, board) == False:
        row = input("What row do you want to place your piece: ")
        column = input("What column do you want to place your piece: ")
    # Perform the move
    board = updateBoard(row, column, board, "X")
    

def main():
    # Creat our board
    board = [["*", "*", "*"],
             ["*", "*", "*"],
             ["*", "*", "*"]]
    # Start our game
    playGame(board)

main()