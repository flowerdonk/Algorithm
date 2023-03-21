from sys import stdin
from collections import deque
stdin = open('input.txt')
'''
포기 에바임
'''
m, n = map(int, stdin.readline().split())
k = int(stdin.readline())
bus = [[[] for _ in range(n)] for _ in range(m)]
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, stdin.readline().split())

    if x1 >= x2:
        x1, x2 = x2, x1
    if y1 >= y2:
        y1, y2 = y2, y1

    for x in range(x1 - 1, x2):
        for y in range(y1 - 1, y2):
            bus[x][y].append(b)
sx, sy, ex, ey = map(int, stdin.readline().split())

visited = [[0] * n for _ in range(m)]
q = deque()
cnt = 1
q.append([sx, sy, cnt])

while q:
    x, y, cnt = q.popleft()
    visited[x][y] = 1

    for n in bus[x][y]:
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and bus[nx][ny]:
                pass