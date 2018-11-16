# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Ashley Wohlrab
# Created: 2018-11-08

symbol = [ " ", "x", "o" ]
#board = [0,0,0,0,0,0,0,0,0]
board = [[0,0,0],[0,0,0],[0,0,0]] 


def printRow(row):
# initialize output to the left border
    output = "|"
# for each square in the row...
    for cell in row:
# add to output the symbol for this square followed by a border
        output += "  " + symbol[cell] + "|"
# print the completed output for this row
    print(output)
pass

def printBoard(board):
    print("+-----------+")
    print("|" + symbol[board[0][0]] + "|" + symbol[board[0][1]] + "|" + symbol[board[0][2]] + "|")
    print("+-----------+")
    print("|" + symbol[board[1][0]] + "|" + symbol[board[1][1]] + "|" + symbol[board[1][2]] + "|")
    print("+-----------+")
    print("|" + symbol[board[2][0]] + "|" + symbol[board[2][1]] + "|" + symbol[board[2][2]] + "|")


def markBoard(board, row, col, player):
    if((row >= 0 and row <= 2) and (col >= 0 and col <= 2)):
        if board[row][col] == 0:
            board[row][col] = player
            return True
        else:
            print("That spot is already taken")
            return False
    else:
        print("That is not a valid location")
        return False
    
 
 # if so, set it to the player number

def checkWins(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != 0:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != 0:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != 0:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != 0:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != 0:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != 0:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != 0:
        return board[2][0]
    else:
        return 0


def getPlayerMove():
    x = input("What row?") # prompt the user separately for the row and column numbers
    y = input("What column?")
    return (x,y) # then return that row and column instead of (0,0)

def hasBlanks(board):
    #for i in board
 # for each row in the board...
 # for each square in the row...
 # check whether the square is blank
 # if so, return True
 return True # if no square is blank, return False

def main():
    player = 1
    while hasBlanks(board) and (checkWins(board) == 0):
        printBoard(board)
        row,col = getPlayerMove()
        if markBoard(board,int(row),int(col),player):
            player = player % 2 + 1 # switch player for next turn
    if checkWins(board) == 0:
        printBoard(board)
        print("No more possible moves, game ends in a tie")
    else:
        printBoard(board)
        print("The winner is " + symbol[checkWins(board)] + "!")
main()


