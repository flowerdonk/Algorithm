import sys
sys.stdin = open('input.txt')
# 줄 단위로 입력, 한 줄씩 중복 없이 받아올 수 있음, 공백 포함

T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    for n in range(2, N - 2):
        if max(data[n - 2 : n + 3]) == data[n]:
            cnt += data[n] - max([data[n - 2], data[n - 1], data[n + 1], data[n + 2]])
    print(f'#{tc} {cnt}')
