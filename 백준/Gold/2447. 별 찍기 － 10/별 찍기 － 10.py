N = int(input())
board = [['*'] * N for _ in range(N)]

def blank(x, y, N):
    l = N // 3
    if board[x][y] == ' ':
        return

    for i in range(l, 2 * l):
        for j in range(l, 2 * l):
            board[x + i][y + j] = ' '

    if l != 1:
        for n in range(3):
            for m in range(3):
                blank(x + n * l,y + m * l, l)
    return

blank(0, 0, N)

for i in range(N):
    for j in range(N):
        print(board[i][j], end='')
    print()