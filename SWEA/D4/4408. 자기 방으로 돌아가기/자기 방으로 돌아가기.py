T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    room = [0] * 200
    cnt = 1

    for n in range(N):
        s, e = data[n][0], data[n][1]
        if s > e:
            s, e = e, s
        for d in range((s - 1) // 2, (e - 1) // 2 + 1):
            room[d] += 1

    print(f'#{tc} {max(room)}')