import sys
sys.stdin = open('input.txt')
def task(idx, n):
    if idx == N:
        mx.append(n)
        return

    for a in data[idx]:
        if a != 0:
            n *= a / 100
            task(idx + 1, n)
            n /= a / 100
        else:
            continue

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)] # idx 직원이 1~N번째 일을 성공할 확률 [, , ...,]
    mx = []
    task(0, 1)
    ans = max(mx) * 100
    print('%.6f'%ans)
