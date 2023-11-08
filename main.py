board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
turnNumber = 1

def checkWin():
    
    board_string = [list(map(str, x)) for x in board]
    rows = [''.join(x) for x in board_string]
    columns = [''.join(x) for x in zip(*board_string)]
    diagonals = [board_string[0][0] + board_string[1][1] + board_string[2][2], board_string[0][2] + board_string[1][1] + board_string[2][0]]
    all = ''.join(rows)
    if 'XXX' in rows or 'XXX' in columns or 'XXX' in diagonals:
        return 'X'
    elif 'OOO' in rows or 'OOO' in columns or 'OOO' in diagonals:
        return 'O'
    elif ' ' not in all:
        return 0
    else:
        return -1
    
def setUp():
    displayBoard()
    while(checkWin() == -1):
        takeTurn()
        displayBoard()
    print(checkWin())
    

def displayBoard():
    for x in board:
        print(' | '.join(x))
        print('_________')
def takeTurn():
    global turnNumber
    while True:
        print("Choose a space, ie (1,2). Top right is (1,1)")
        command = [x - 1 for x in map(int, input().split(","))]
        space = board[command[0]][command[1]]
        if space == ' ':
            print(turnNumber)
            board[command[0]][command[1]] = 'O' if (turnNumber % 2 == 0) else 'X'
            turnNumber += 1
            break

        else:
            print("Invalid space, try again")
    #displayBoard()
         

setUp()