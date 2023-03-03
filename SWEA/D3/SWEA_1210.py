import sys
sys.stdin = open('input.txt')

T = 10
N = 100
for tc in range(1, T + 1):
    _ = input()
    data = [list(input().split()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    end_i, end_j = 0, 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '2':
                end_i, end_j = i, j

    direction = [[0, -1], [0, 1]] # 왼쪽, 오른쪽, 위
    si, sj = end_i, end_jc
    while si != 0:
        visited[si][sj] = 1
        for d in direction:
            ni = si + d[0]
            nj = sj + d[1]
            while 0 <= ni < N and 0 <= nj < N and data[ni][nj] == '1' and visited[ni][nj] == 0:
                visited[si][sj] = 1
                si = ni
                sj = nj
                ni += d[0]
                nj += d[1]
        si -= 1
    print(f'#{tc} {sj}')