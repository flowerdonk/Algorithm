import sys
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
v = []
data = []
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = []
emptycnt = 0

for n in range(N):
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    for m in range(N):
        if l[m] == 2:
            v.append([n, m])
        elif l[m] == 0:
            emptycnt += 1
    data.append(l)

if emptycnt == 0:
    print(0)

else:
    subset = list(combinations(v, M))

    for sub in subset:
        visited = [[-1] * N for _ in range(N)]
        q = deque()

        for i, j in sub:
            visited[i][j] = 0
            q.append([i, j])

        mx = 0
        while q:
            i, j = q.popleft()

            for di, dj in direction:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0<= nj < N:
                    if data[ni][nj] == 0 and visited[ni][nj] == -1:
                        q.append([ni, nj])
                        visited[ni][nj] = visited[i][j] + 1
                        mx = visited[ni][nj]
                    elif data[ni][nj] == 2 and visited[ni][nj] == -1:
                        q.append([ni, nj])
                        visited[ni][nj] = visited[i][j] + 1


        for i in range(N):
            if mx == 10000:
                break
            for j in range(N):
                if data[i][j] == 0 and visited[i][j] == -1:
                    mx = 10000
                    break

        ans.append(mx)

    mn = min(ans)
    if mn == 10000:
        print(-1)
    else:
        print(mn)