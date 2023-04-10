'''Backtracking
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
'''
'''
# greedy
T = int(input())
for tc in range(1, T + 1):
    D, M, T, Y = map(int, input().split())
    data = [0] + list(map(int, input().split()))

    s = [0] * 13
    for i in range(1, 13):
        # 가능한 방법 중 i달까지의 최소 비용
        s[i] = s[i - 1] + D * data[i] # 일간권
        s[i] = min(s[i], s[i - 1] + M) # 월간권
        if i >= 3:
            s[i] = min(s[i], s[i - 3] + T) # 월간권 - 3달
        if i >= 12:
            s[i] = min(s[i], s[i - 12] + Y) # 연간권

    ans = s[12]
    print(f'#{tc} {ans}')
'''
def dfs(n, total):
    global ans

    if n > 12:
        ans = min(ans, total)
        return

    dfs(n + 1, total + day * plan[n])
    dfs(n + 1, total + mon)
    dfs(n + 3, total + mon3)
    dfs(n + 12, total + year)


T = int(input())
for tc in range(1, T + 1):
    ans = 0
    day, mon, mon3, year = map(int, input().split())
    plan = list(map(int, input().split()))

    print(f'#{tc} {ans}')
