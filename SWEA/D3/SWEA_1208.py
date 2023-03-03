import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    for n in range(N):
        mx_idx = data.index(max(data))
        mn_idx = data.index(min(data))
        data[mx_idx] -= 1
        data[mn_idx] += 1

    print(f'#{tc} {max(data) - min(data)}')