n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
ans = 0

def check(r, c):
    if 0 < r < n and 0 < c < m:
        first = dp[r-1][c-1]
        second = dp[r-1][c]
        third = dp[r][c-1]
        return min(first, second, third) + 1
    return 1

for r in range(n):
    for c in range(m):
        if board[r][c] == '1':
            dp[r][c] = check(r, c)
            ans = max(ans, dp[r][c])

print(ans**2)