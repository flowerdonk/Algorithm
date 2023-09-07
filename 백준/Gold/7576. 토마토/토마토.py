from collections import deque

M, N = map(int, input().split())
board = [] # 1 익은 토마토, 0 익지 않은 토마토, -1 토마토 X
for n in range(N):
    board.append(list(input().split()))

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[0] * M for _ in range(N)]
q = deque()

cnt = 0
for bi in range(N):
    for bj in range(M):
        if board[bi][bj] == '1':
            q.append((bi, bj))
            cnt += 1
        elif board[bi][bj] == '-1':
            cnt += 1

ans = 0
while q:
    si, sj = q.popleft()

    for d in direction:
        ni, nj = si + d[0], sj + d[1]

        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and board[ni][nj] == '0':
            q.append((ni, nj))
            visited[ni][nj] = visited[si][sj] + 1
            ans = visited[ni][nj]

temp = 0
for visit in visited:
    for v in visit:
        if v == 0:
            temp += 1

if cnt < temp:
    print(-1)
else:
    print(ans)