board = []
blank = []

for n in range(9):
    temp = list(map(int, input().split()))
    for m in range(9):
        if temp[m] == 0:
            blank.append((n, m))
    board.append(temp)


# 해당 idx에 n이 있는지 확인
def row(idx, n):
    for i in range(9):
        if board[idx][i] == n:
            return False
    return True

def column(idx, n):
    for i in range(9):
        if board[i][idx] == n:
            return False
    return True

def square(x, y, n):
    for i in range(3):
        for j in range(3):
            if board[y//3 * 3 + i][x//3 * 3 + j] == n:
                return False
    return True

# n 번째 빈칸
def dfs(n):
    # 빈칸 수에 닿을 경우
    if n == len(blank):
        for b in board:
            print(*b)
        exit()

    for num in range(1, 10):
        y = blank[n][0]
        x = blank[n][1]
        if row(y, num) and column(x, num) and square(x, y, num):
            board[y][x] = num
            dfs(n + 1)
            board[y][x] = 0

dfs(0)