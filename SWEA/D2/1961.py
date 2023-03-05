import sys
sys.stdin = open('input.txt')

T = int(input())
for n in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    a1 = [[0] * N for _ in range(N)] # 90
    a2 = [[0] * N for _ in range(N)] # 180
    a3 = [[0] * N for _ in range(N)] # 270

    ## 1번째 방법 - 반복문
    # 회전 각도에 따른 위치값 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N - 1 - j][i]
            a2[i][j] = arr[N - 1 - i][N - 1 - j]
            a3[i][j] = arr[j][N - 1 - i]

    print(f'#{n}')

    for a, b, c in zip(a1, a2, a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')

    ## 2번째 방법 - 리스트 슬라이싱
    arr_t = list(map(list, zip(*arr)))

    print(f'#{n}')

    for i in range(N):
        print(f'{"".join(arr_t[i][::-1])} {"".join(arr_t[N - 1 - i][::-1])} {"".join(arr_t[N - 1 - i])}')