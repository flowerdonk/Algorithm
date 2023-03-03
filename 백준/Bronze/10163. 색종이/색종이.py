N = int(input())
data = [list(map(int, input().split())) for _ in range(N)] # [왼쪽 아래 y, x, w, h]
board = [[0] * 101 for _ in range(101)]

for n in range(1, N + 1):
    y, x, w, h = data[n - 1]
    for i in range(y, y + w):
        for j in range(x, x + h):
            board[i][j] = n

ans = [0] + [0] * N
for i in range(101):
    for j in range(101):
        if board[i][j]:
            ans[board[i][j]] += 1

for a in ans[1:]:
    print(a)