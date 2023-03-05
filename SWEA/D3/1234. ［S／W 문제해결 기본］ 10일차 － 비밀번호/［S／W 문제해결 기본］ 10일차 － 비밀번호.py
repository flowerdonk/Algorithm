T = 10
for tc in range(1, T + 1):
    _, data = input().split()
    result = ''
    cnt = 1
    while cnt:
        N = len(data)
        for n in range(N - 1):
            if data[n] == data[n + 1]:
                data = data[ : n] + data[n + 2: ]
                cnt = 1
                break
            else:
                cnt = 0

    print(f'#{tc} {data}')