T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    adjM = [[] for _ in range(N + 1)]

    for m in range(M):
        n1, n2 = data[m * 2], data[m * 2 + 1]
        adjM[n1].append(n2)
        adjM[n2].append(n1)

    q = []
    cnt = 0
    visited = [0] * (N + 1)

    for n in range(1, N + 1):
        if visited[n] == 1:
            continue
        else:
            visited[n] = 1
            for num in adjM[n]:
                q.append(num)

            while q:
                s = q.pop(0)
                if visited[s] == 1:
                    continue
                else:
                    visited[s] = 1

                    for ss in adjM[s]:
                        q.append(ss)

            cnt += 1
    print(f'#{tc} {cnt}')