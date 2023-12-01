from Sudoku_Board_Validifier import is_valid_sudoku

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


def solve(board, row=0, col=0):
    if row == 9:
        return True
    elif col == 9:
        return solve(board, row + 1, 0)
    elif board[row][col] != ".":
        return solve(board, row, col + 1)
    else:
        for attempt_num in range(1, 10):
            if is_valid_sudoku(board):
                board[row][col] = str(attempt_num)
                if solve(board, row, col + 1):
                    return board
                board[row][col] = "."
        return False


solve(board)


