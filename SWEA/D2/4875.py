import sys
sys.stdin = open('input.txt')

def maze(N, arr):

    # 0 : 오른쪽, 1 : 아래, 2 : 왼쪽, 3 : 위쪽
    dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N): # 시작점, 도착점 조사
        for j in range(N):
            if arr[i][j] == 2:
                start_x, start_y = i, j

    stack = [(start_x, start_y)] # 갈림길 스택
    visited[start_x][start_y] = 1

    while stack: # 스택이 비어있지 않을 때
        x, y = stack.pop() # 스택 마지막을 좌표로 (이전 좌표로)
        visited[x][y] = 1 # 방문 완료

        for i in range(4):
            nx = x + dij[i][0]
            ny = y + dij[i][1]

            # 경계 검사
            if nx < 0 or nx == N or ny < 0 or ny == N:
                continue

            if arr[nx][ny] == 3:
                return 1

            elif not arr[nx][ny] and not visited[nx][ny]: # 모두 0일 때
                stack.append((nx, ny))

    return 0


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    print(f'#{i} {maze(N, arr)}')