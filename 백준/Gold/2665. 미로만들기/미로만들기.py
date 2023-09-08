from heapq import heappush, heappop

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

heap = []
heappush(heap, [0, 0, 0])
visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

while heap:
    change, i, j = heappop(heap)

    if i == n - 1 and j == n - 1:
        print(change)

    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            if board[ni][nj] == '0':
                heappush(heap, [change + 1, ni, nj])
            else:
                heappush(heap, [change, ni, nj])
