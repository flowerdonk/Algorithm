C, R = map(int, input().split()) # 가로, 세로
K = int(input())
board = [[0] * C for _ in range(R)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[0] * C for _ in range(R)]
visited[0][0] = 1
d_idx = 0
c, r = 0, 0
cnt = 1
ans = (0, 0)

if K > C * R:
    print(0)
else:
    while cnt <= C * R:
        visited[r][c] = cnt
        if cnt == K:
            ans = (c + 1, r + 1)
            break
        nc, nr = c + direction[d_idx][0], r + direction[d_idx][1]
        if 0 <= nc < C and 0 <= nr < R and visited[nr][nc] == 0:
            c = nc
            r = nr
            cnt += 1
        else:
            d_idx = (d_idx + 5) % 4

    print(*ans)