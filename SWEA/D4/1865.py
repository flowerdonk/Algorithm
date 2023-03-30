import sys
sys.stdin = open('input.txt')
def task(i, n):
    global mx

    if n <= mx:
        return

    if i == N:
        mx = max(mx, n)
        return

    for j in range(N):
        if data[i][j] != 0:
            if not visited[j]:
                new_n = n * data[i][j] / 100
                visited[j] = 1
                task(i + 1, new_n)
                visited[j] = 0
        else:
            continue

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)] # idx 직원이 1~N번째 일을 성공할 확률 [, , ...,]
    visited = [0] * N
    mx = 0
    task(0, 1)
    mx *= 100
    print(f'#{tc} ', end="")
    print('%.6f'%mx)
