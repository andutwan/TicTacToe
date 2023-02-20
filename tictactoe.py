# Checks to see if there is a horizontal win
def horizontalWin(board):
    # Keeps track of how many X there are and O by row
    xCounter = 0
    oCounter = 0
    blankCounter = 9
    # Iterates through the rows
    for row in range(3):
        # Iterates through the cols
        for col in range(3):
            # Checks to see if the spot is occupied by an X or O
            if board[row][col] == "X":
                # Increase xCounter if you see an X
                xCounter += 1
                blankCounter -= 1
            elif board[row][col] == "O":
                # Increase oCounter if you see an O
                oCounter += 1
                blankCounter -= 1
        # Check to see if there was 3 X or O in a row and if theres a tie
        if xCounter == 3 or oCounter == 3 or blankCounter == 0:
            return True
        # Reset our counters
        xCounter = 0
        oCounter = 0
    
    # Return False if there is no win
    return False

# Checks to see if there is a vertical win
def verticalWin(board):
    # Keeps track of how many X there are and O by row
    xCounter = 0
    oCounter = 0
    blankCounter = 9
    # Iterates through the rows
    for col in range(3):
        # Iterates through the cols
        for row in range(3):
            # Checks to see if the spot is occupied by an X or O
            if board[row][col] == "X":
                # Increase xCounter if you see an X
                xCounter += 1
                blankCounter -= 1
            elif board[row][col] == "O":
                # Increase oCounter if you see an O
                oCounter += 1
                blankCounter -= 1
        # Check to see if there was 3 X or O in a row
        if xCounter == 3 or oCounter == 3 or blankCounter == 0:
            return True
        # Reset our counters
        xCounter = 0
        oCounter = 0
    
    # Return False if there is no win
    return False

# Checks to see if there is a diagonal win
def diagonalWin(board):
    # # Keeps track of how many X there are and O by row
    # xCounter = 0
    # oCounter = 0
    # blankCounter = 0
    # # Iterates through the rows
    # for row in range(3):
    #     # Iterates through the cols
    #     for col in range(3):
    #         # If row == col, we are at a diagonal
    #         if row == col:
    #             # Checks to see if the spot is occupied by an X or O
    #             if board[row][col] == "X":
    #                 # Increase xCounter if you see an X
    #                 xCounter += 1
    #             elif board[row][col] == "O":
    #                 # Increase oCounter if you see an O
    #                 oCounter += 1
    #             else:
    #                 blankCounter += 1
    #     # Check to see if there was 3 X or O in a row
    #     if xCounter == 3 or oCounter == 3 or blankCounter == 0:
    #         return True
    #     # Reset our counters
    #     xCounter = 0
    #     oCounter = 0
    
    # # Return False if there is no win
    return False

#Checks to see if the game is over
def gameover(board):
    return horizontalWin(board) or verticalWin(board) or diagonalWin(board)

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

    # Game loop
    #Continue game until there is a winner or a tie
    while gameover(board) == False:
        # Ask user for their move
        row = int(input("What row do you want to place your piece: "))
        column = int(input("What column do you want to place your piece: "))
        # Check if the move is valid
        while validInput(row, column, board) == False:
            row = input("What row do you want to place your piece: ")
            column = input("What column do you want to place your piece: ")
        # Perform the move
        board = updateBoard(row, column, board, "X")
        # AI move

    print("You win!")
    

def main():
    # Creat our board
    board = [["*", "*", "*"],
             ["*", "*", "*"],
             ["*", "*", "*"]]
    # Start our game
    playGame(board)

main()