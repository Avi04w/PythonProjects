def make_board(board):
    print(" " + board[0] + " | " + " " + board[1] + " | " + " " + board[2])
    print("-------------")
    print(" " + board[3] + " | " + " " + board[4] + " | " + " " + board[5])
    print("-------------")
    print(" " + board[6] + " | " + " " + board[7] + " | " + " " + board[8])


def player_move(board):
    p_move = input("Type in a number from 1-9 to place your X on the board ")
    p_move = int(p_move) - 1
    board[p_move] = "X"
    make_board(board)


def free_space(board, m):
    return board[m] == " "


def get_board_copy(board):
    copy_board = []
    for i in board:
        copy_board.append(i)
    return copy_board


def comp_move(board):
    for i in range(0, 9):
        copy = get_board_copy(board)
        if free_space(copy, i):
            copy[i] = "O"
            if check_winner(copy, "O"):
                return i

    for i in range(0, 9):
        copy = get_board_copy(board)
        if free_space(copy, i):
            copy[i] = "X"
            if check_winner(copy, "X"):
                return i

    if free_space(board, 4):
        return 4

    corner_moves = [4, 0, 2, 6, 8]
    for i in corner_moves:
        if free_space(board, i):
            return i

    side_moves = [1, 3, 5, 7]
    for i in side_moves:
        if free_space(board, i):
            return i


def check_winner(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark))


def make_move(board, letter, move1):
    board[move1] = letter


def board_is_full(board):
    for i in range(0, 9):
        if board[i] == " ":
            return False
    return True


print("Welcome to Tic Tac Toe!")
print("You are 'X' and I will be 'O'")
print("You go first!")
game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
make_board(game_board)

game_running = True

while game_running:
    player_move(game_board)
    win = check_winner(game_board, "X")
    if win:
        print("Congratulations, You Win!")
        break
    full_board = board_is_full(game_board)
    if full_board:
        print("We Tied!")
        break
    move = comp_move(game_board)
    make_move(game_board, "O", move)
    make_board(game_board)
    win = check_winner(game_board, "O")
    if win is True:
        print("I Win! Better luck next time!")
        break