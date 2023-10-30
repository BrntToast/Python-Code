board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turnNumber = 1

def checkWin():
    
    board_string = [list(map(str, x)) for x in board]
    rows = [''.join(x) for x in board_string]
    columns = [''.join(x) for x in zip(*board_string)]
    diagonals = [board_string[0][0] + board_string[1][1] + board_string[2][2], board_string[0][2] + board_string[1][1] + board_string[2][0]]
    all = ''.join(rows)
    if '111' in rows or '111' in columns or '111' in diagonals:
        return 1
    elif '222' in rows or '222' in columns or '222' in diagonals:
        return 2
    elif '0' not in all:
        return 0
    else:
        return -1
    
def setUp():
    displayBoard()
    while(checkWin() == -1):
        takeTurn()
        displayBoard()
    print()
    

def displayBoard():
    for x in board:
        #line = map(str, ["O" if i == 1 else if "X" for i in x])
        #print(' | '.join(line))
        print('_________')
def takeTurn():
    global turnNumber
    while True:
        print("Choose a space, ie (1,2). Top right is (1,1)")
        command = [x - 1 for x in map(int, input().split(","))]
        space = board[command[0]][command[1]]
        if space == 0:
            print(turnNumber)
            board[command[0]][command[1]] = 2 if (turnNumber % 2 == 0) else 1
            turnNumber += 1
            break

        else:
            print("Invalid space, try again")
    #displayBoard()
         

setUp()