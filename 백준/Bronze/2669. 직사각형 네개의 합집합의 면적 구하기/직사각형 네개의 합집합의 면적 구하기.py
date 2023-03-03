data = [list(map(int, input().split())) for _ in range(4)] # [왼쪽아래 x, y, 오른쪽위 x, y]
_, _, _, Y = max(data, key = lambda x:x[3])
_, _, X, _ = max(data, key = lambda x:x[2])
board = [[0] * X for _ in range(Y)]

for n in range(4):
    x, y, p, q = data[n]
    for i in range(y, q):
        for j in range(x, p):
            board[i][j] = 1

cnt = 0
for i in range(Y):
    for j in range(X):
        if board[i][j] == 1:
            cnt += 1

print(cnt)