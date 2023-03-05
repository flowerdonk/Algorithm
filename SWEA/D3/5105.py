import sys
sys.stdin = open('input.txt')

def maze(N, arr):
    arr_i = ''.join(arr)
    start_x, start_y = divmod(arr_i.index('2'), N)
    end_x, end_y = divmod(arr_i.index('3'), N)

    visited = [[0] * N for _ in range(N)]
    Q = [(start_x, start_y)]
    visited[start_x][start_y] = 1

    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while Q:
        x, y = Q.pop(0)
        sx, sy = x, y

        for d in direction:
            nx, ny = sx + d[0], sy + d[1]
            if 0 <= nx < N and 0 <= ny < N: # 패딩 안되어있어서
                if arr[nx][ny] != '1' and visited[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[sx][sy] + 1
                    if nx == end_x and ny == end_y:
                        return (visited[nx][ny] - 2)

    return 0

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{i} {maze(N, arr)}')