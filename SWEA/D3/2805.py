def farm(N, arr):
    result = 0
    # 수확 땅 넓이 [1, 3, 5, 3, 1]...
    harvest = [i * 2 + 1 for i in range((N + 1)//2)] + [j * 2 - 1 for j in range((N - 1)//2, 0, -1)]

    for i in range(N):
        start = (N - harvest[i]) // 2 # 중앙 수확지점 시작부터
        for j in range(start, start + harvest[i]): # 수확 땅 수만큼
            result += arr[i][j]

    return result

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    print(f'#{i} {farm(N, arr)}')