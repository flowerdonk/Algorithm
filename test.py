import sys
sys.stdin = open('input.txt')

N = int(input())
ans = 0
dp = [0] * (N + 1)

if not N % 2: # 짝수일 때
    dp[2] = 3
    for n in range(4, N + 1, 2): # 4부터 짝수만
        dp[n] = dp[2] * dp[n - 2] + 2
        for m in range(4, n, 2): # 4칸을 차지하는 특수한 경우 2씩 추가
            dp[n] += 2 * dp[n - m]

ans = dp[N]
print(ans)