T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1

    for n in range(M):
        i, j, c = data[n]
        i -= 1
        j -= 1
        board[i][j] = c
        for d in ([-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]):
            temp = []
            for m in range(1, N):
                ni, nj = i + d[0] * m, j + d[1] * m
                if 0 <= ni < N and 0 <= nj < N:
                    if board[ni][nj] == 0:
                        break
                    elif board[ni][nj] != c:
                        temp.append((ni, nj))
                    else:
                        while temp:
                            ti, tj = temp.pop()
                            board[ti][tj] = c
                        break

    bcnt, wcnt = 0, 0
    for l in board:
        bcnt += l.count(1)
        wcnt += l.count(2)

    print(f'#{tc} {bcnt} {wcnt}')