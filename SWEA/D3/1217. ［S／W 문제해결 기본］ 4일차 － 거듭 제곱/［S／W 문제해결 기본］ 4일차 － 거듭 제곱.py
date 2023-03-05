def power(N, M):
    if M == 0:
        return 1
    else:
        return N * power(N, M - 1)

T = 10
for tc in range(1, T + 1):
    _ = input()
    N, M = map(int, input().split())
    print(f'#{tc} {power(N, M)}')