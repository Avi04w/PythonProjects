num_rows = int(input())
num_columns = int(input())
strokes = int(input())

board = [[0 for y in range(num_columns)] for x in range(num_rows)]
moves = [input() for i in range(strokes)]


def brush_stroke(b, move):
    move = move.split(" ")
    m = int(move[1]) - 1

    if move[0] == "R":
        b[m] = [1 - y for y in b[m]]
    else:
        for x in range(num_rows):
            b[x][m] = 1 - b[x][m]

    return b


for i in moves:
    board = brush_stroke(board, i)

print(sum(map(sum, board)))