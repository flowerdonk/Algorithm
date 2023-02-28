N = int(input())
L = 10 # 색종이 길이
data = [list(map(int, input().split())) for _ in range(N)] # x, y
length_idx, _ = max(data, key = lambda x : x[0])
_, height_idx = max(data, key = lambda x : x[1])
board = [[0] * (length_idx + L + 1) for _ in range(height_idx + L + 1)]

for n in range(N):
    x = data[n][0]
    y = data[n][1]
    for i in range(L):
        for j in range(L):
            board[y + i][x + j] = 1

cnt = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 1:
            cnt += 1

print(cnt)