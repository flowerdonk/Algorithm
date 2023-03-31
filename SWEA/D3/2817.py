def dfs(depth, total):
    global ans

    if K < total:
        return

    if depth == N:
        if total == K:
            ans += 1
        return

    dfs(depth + 1, total + data[depth])
    dfs(depth + 1, total)

T = int(input())
for tc in range(1,T + 1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [0] * N
    ans = 0
    dfs(0, 0)
    print(f'#{tc} {ans}')