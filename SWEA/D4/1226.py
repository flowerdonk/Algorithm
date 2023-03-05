import sys
sys.stdin = open('input.txt')

def maze(arr):
    # 시작점, 끝점 찾기
    arr_i = ''.join(arr)
    start_x, start_y = divmod(arr_i.index('2'), N)
    end_x, end_y = divmod(arr_i.index('3'), N)

    # visited = [[0] * N] * N 이렇게 하면 13번 줄에서 오류 발생
    visited = [[0] * N for _ in range(N)]
    Q = [(start_x, start_y)] # 이동 가능한 좌표들?
    visited[start_x][start_y] = 1

    # 인접 지점 찾기
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while Q: # 이동 가능한 좌표들 모두 확인
        x, y = Q.pop(0)
        sx, sy = x, y # 반복문에 사용하기 위해 변수에 저장

        for d in direction: # 4방향 탐색
            nx, ny = sx + d[0], sy + d[1] # 이동할 좌표
            if arr[nx][ny] != '1' and visited[nx][ny] == 0:
                Q.append((nx, ny)) # 이동 가능한 좌표들 모두 담기
                visited[nx][ny] = visited[x][y] + 1 # 이동하는 순서대로 수 입력


    if visited[end_x][end_y] != 0: # 끝 지점에 방문했다면
        return 1
    else:
        return 0

T = 10
N = 16
for _ in range(1, T + 1):
    tc = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {maze(arr)}')