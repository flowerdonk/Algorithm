from collections import deque

global ans
ans = 0

board = []
for r in range(12):
    board.append(list(input()))

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(si, sj, board):
    global ans
    visited = [[0] * 6 for _ in range(12)]
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    color = board[si][sj]
    cnt = 1
    temp = [(si, sj)]

    while q:
        i, j = q.popleft()

        for d in dirs:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < 12 and 0 <= nj < 6 and visited[ni][nj] == 0 and board[ni][nj] == color:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
                temp.append((ni, nj))

    if cnt >= 4:
        ans += 1
        for ti, tj in temp:
            board[ti][tj] = '.'

flag = True
answer = 0
while flag:
    pre_ans = ans
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                dfs(i, j, board)
    post_ans = ans
    if pre_ans == post_ans:
        flag = False
    else:
        answer += 1
        for m in range(6):
            temp_q = deque()
            for n in range(11, -1, -1):
                if board[n][m] != '.':
                    temp_q.append(board[n][m])
            idx = 11
            while temp_q:
                board[idx][m] = temp_q.popleft()
                idx -= 1
            while idx >= 0:
                board[idx][m] = '.'
                idx -= 1
print(answer)