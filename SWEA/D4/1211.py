import sys
sys.stdin = open('input.txt')

N = 100
T = 10
for tc in range(1, T + 1):
    _ = input()
    data = [list(input().split()) for _ in range(N)]
    start = []
    result = []

    for n in range(N):
        if data[0][n] == '1':
            start.append((0, n))

    for s in start:
        stack = []
        visited = [[0] * N for _ in range(N)]
        visited[s[0]][s[1]] = 1
        stack.append(s)
        while stack:
            i, j = stack.pop(0)
            if i == N - 1:
                result.append((s[1], visited[i][j]))

            post_len = len(stack)
            for d in ([0, -1], [0, 1]):
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and data[ni][nj] == '1':
                    stack.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

            if post_len == len(stack):
                if 0 <= i + 1 < N and 0 <= j < N and visited[i + 1][j] == 0 and data[i + 1][j] == '1':
                    stack.append((i + 1, j))
                    visited[i + 1][j] = visited[i][j] + 1

    print(f'#{tc} {min(result, key = lambda x : x[1])[0]}')
