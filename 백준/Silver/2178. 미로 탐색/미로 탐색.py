from collections import deque

N, M = map(int, input().split())
board = []
for n in range(N):
    board.append(list(input()))

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[0] * M for _ in range(N)]
q = deque()
q.append((0, 0))
visited[0][0] = 1

while q:
    i, j = q.popleft()

    for d in direction:
        ni, nj = i + d[0], j + d[1]

        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and board[ni][nj] == '1':
            q.append((ni, nj))
            visited[ni][nj] = visited[i][j] + 1

print(visited[N - 1][M - 1])