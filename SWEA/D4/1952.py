def dfs(n, sm):
    global ans

    if ans <= sm:
        return

    if n > 12:
        ans =  min(ans, sm)
        return

    dfs(n + 1, sm + D * data[n])
    dfs(n + 1, sm + M)
    dfs(n + 3, sm + T)
    dfs(n + 12, sm + Y)

T = int(input())
for tc in range(1, T + 1):
    D, M, T, Y = map(int, input().split())
    data = [0] + list(map(int, input().split()))

    ans = 365 * 3000
    dfs(1, 0)

    print(f'#{tc} {ans}')