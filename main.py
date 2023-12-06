# Global variables for keeping track of game state
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
turnNumber = 1

# Checks for a win or a tie in the current game
def checkWin():
        # Create a list of all rows, columns, and diagonals in the current game state
    board_string = [list(map(str, x)) for x in board]
    rows = [''.join(x) for x in board_string]
    columns = [''.join(x) for x in zip(*board_string)]
    diagonals = [board_string[0][0] + board_string[1][1] + board_string[2][2], board_string[0][2] + board_string[1][1] + board_string[2][0]]

    # Combine all rows, columns, and diagonals into a single string
    all = ''.join(rows)

    # Check for three in a row
    if 'XXX' in rows or 'XXX' in columns or 'XXX' in diagonals:
        return 'X'
    elif 'OOO' in rows or 'OOO' in columns or 'OOO' in diagonals:
        return 'O'
    
    # Check for tie
    elif ' ' not in all:
        return 0
    else:
        return -1


def setUp():
    # Display the current game board
    displayBoard()

    # Keep taking turns until there is a win or a tie
    while(checkWin() == -1):
        takeTurn()
        displayBoard()
    
    # Print the result of the game
    print(checkWin())
    

def displayBoard():
    # Print each row of the game board with the pipe character as a seperator
    for x in board:
        print(' | '.join(x))
        print('_________')
def takeTurn():
    global turnNumber
    while True:
        print("Choose a space, ie (1,2). Top right is (1,1)")

        # Ask the user for their move
        command = [x - 1 for x in map(int, input().split(","))]
        space = board[command[0]][command[1]]

        # Ensures the space is empty
        if space == ' ':
            print(turnNumber)
            board[command[0]][command[1]] = 'O' if (turnNumber % 2 == 0) else 'X'
            turnNumber += 1
            break

        else:
            print("Invalid space, try again")
    #displayBoard()

setUp()