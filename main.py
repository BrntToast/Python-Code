def main(board):
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